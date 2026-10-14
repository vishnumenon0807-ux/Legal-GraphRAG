"""Run the retrieval ablation: expansion off vs on. STAGE 3/4.

    python scripts/run_baseline.py
    python scripts/run_baseline.py --k 10 --base-k 10

Reports recall, precision and gold_coverage (every required section retrieved)
for the base retriever and for several expansion settings, so the effect of
expansion is visible rather than asserted.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from legalgraph import config  # noqa: E402
from legalgraph.benchmark import validate  # noqa: E402
from legalgraph.eval import metrics  # noqa: E402
from legalgraph.retrieval import corpus  # noqa: E402
from legalgraph.retrieval.bm25 import BM25Retriever  # noqa: E402
from legalgraph.retrieval.expand import expand  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=10, help="cutoff the metrics are computed at")
    ap.add_argument("--base-k", type=int, default=10, help="base results fetched before expansion")
    ap.add_argument("--k1", type=float, default=1.5)
    ap.add_argument("--b", type=float, default=0.75)
    args = ap.parse_args()

    nodes = json.loads(config.CLAUSES.read_text(encoding="utf-8"))
    edges = json.loads(config.EDGES.read_text(encoding="utf-8"))
    questions, errors = validate.load(config.QUESTIONS)
    if errors:
        raise SystemExit(f"benchmark has {len(errors)} problem(s); run validate_benchmark.py")

    units = corpus.build_units(nodes)
    graph = corpus.section_graph(nodes, edges)
    bigraph = corpus.add_reverse(graph)
    retriever = BM25Retriever(units, k1=args.k1, b=args.b)

    print(f"corpus: {len(units)} sections | graph: "
          f"{sum(len(v) for v in graph.values())} directed edges, "
          f"{sum(len(v) for v in bigraph.values())} bidirectional")
    print(f"questions: {len(questions)} | k={args.k} base_k={args.base_k}")
    print()

    # one base run, reused by every expansion setting so the comparison is exact
    base_hits = {q.id: retriever.search(q.question, k=args.base_k) for q in questions}
    gold = {q.id: corpus.gold_sections(q.gold_clauses) for q in questions}

    # FIXED CONTEXT BUDGET. Every setting returns at most k sections, so the
    # question is what those k slots are SPENT on, not how many you get.
    # Expansion trades lexical hits ranked base_n+1..k for referenced sections.
    # Giving expansion extra slots on top of a full base ranking would raise
    # recall for free and prove nothing.
    settings = [
        ("no expansion", args.k, 0, None, graph),
        ("base 8 + d1", 8, 1, 3, graph),
        ("base 6 + d1", 6, 1, 3, graph),
        ("base 5 + d1", 5, 1, None, graph),
        ("base 5 + d2", 5, 2, 3, graph),
        ("base 3 + d1", 3, 1, None, graph),
        ("base 6 + d1 both ways", 6, 1, 3, bigraph),
        ("base 5 + d1 both ways", 5, 1, None, bigraph),
    ]

    print(f"{'setting':<22} {'recall':>7} {'prec':>7} {'covered':>8} {'mean |ret|':>11}")
    print("-" * 60)
    rows = {}
    for name, base_n, depth, seeds, g in settings:
        runs, sizes = [], []
        for q in questions:
            seed_list = base_hits[q.id][:base_n]
            ret = expand(seed_list, g, depth=depth, seeds=seeds)[:args.k]
            runs.append((ret, gold[q.id]))
            sizes.append(len(ret))
        m = metrics.evaluate(runs, k=args.k)
        rows[name] = (m, runs)
        print(f"{name:<22} {m['recall@k']:>7.3f} {m['precision@k']:>7.3f} "
              f"{m['gold_coverage']:>8.3f} {sum(sizes)/len(sizes):>11.1f}")

    # Which questions does expansion actually rescue? That list is the argument.
    base_m, base_runs = rows["no expansion"]
    exp_m, exp_runs = rows["base 5 + d1 both ways"]
    rescued, broken = [], []
    for q, (br, g), (er, _) in zip(questions, base_runs, exp_runs, strict=True):
        b_ok = metrics.fully_covered(br, g, args.k)
        e_ok = metrics.fully_covered(er, g, args.k)
        if e_ok and not b_ok:
            rescued.append(q)
        elif b_ok and not e_ok:
            broken.append(q)

    print()
    print(f"expansion (base 5 + d1 both ways) rescued {len(rescued)}, broke {len(broken)}")
    for q in rescued:
        missing = [s for s in gold[q.id] if s not in base_hits[q.id][:args.k]]
        print(f"  + {q.id} missing {missing} from base: {q.question[:62]}")
    for q in broken:
        print(f"  - {q.id} pushed out of top-{args.k}: {q.question[:62]}")

    # Questions nothing finds. If these dominate, the retriever is the problem,
    # not the absence of a graph.
    print()
    never = [q.id for q, (er, g) in zip(questions, exp_runs, strict=True)
             if not metrics.fully_covered(er, g, args.k)]
    print(f"still uncovered with expansion: {len(never)}/{len(questions)}  {never}")

    out = config.BENCHMARK.parent / "results_bm25.json"
    out.write_text(json.dumps(
        {name: m for name, (m, _) in rows.items()}, indent=2), encoding="utf-8")
    print(f"\nmetrics -> {out.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
