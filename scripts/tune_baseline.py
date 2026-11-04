"""Find the strongest honest BM25 baseline, then re-test expansion against it.

    python scripts/tune_baseline.py

Why tuning on the evaluation set is acceptable HERE and nowhere else: the search
maximises the BASELINE's score, which is adversarial to the claim being made.
Picking the baseline configuration that makes the graph look worst is the
opposite of overfitting in your own favour. The expansion settings are NOT
tuned the same way; they inherit whatever the best baseline chose.

If the graph's advantage disappears under a tuned baseline, that is the finding
and it needs reporting, not retuning.
"""

import argparse
import itertools
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


def heading_weight_units(nodes, repeats: int):
    """Rebuild units with the heading repeated `repeats` times.

    The heading is the most topical few words in a section and otherwise drowns
    in 2,000 words of operative text, so how hard it is weighted is a real
    baseline-strength knob, not a trick.
    """
    units = []
    for n in nodes:
        if n["type"] != "section":
            continue
        text = n.get("full_text") or n.get("text") or ""
        if not text.strip():
            continue
        h = n.get("heading", "")
        prefix = (h + ". ") * repeats
        units.append({"id": n["id"], "heading": h, "text": prefix + text, "raw": text})
    return units


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=10)
    args = ap.parse_args()

    nodes = json.loads(config.CLAUSES.read_text(encoding="utf-8"))
    edges = json.loads(config.EDGES.read_text(encoding="utf-8"))
    questions, errors = validate.load(config.QUESTIONS)
    if errors:
        raise SystemExit(f"benchmark has {len(errors)} problem(s)")

    graph = corpus.section_graph(nodes, edges)
    bigraph = corpus.add_reverse(graph)
    gold = {q.id: corpus.gold_sections(q.gold_clauses) for q in questions}

    k1s = [0.9, 1.2, 1.5, 1.8, 2.2]
    bs = [0.3, 0.5, 0.75, 0.9]
    heads = [0, 1, 2, 4]

    print(f"sweeping {len(k1s)*len(bs)*len(heads)} baseline configs "
          f"on {len(questions)} questions, k={args.k}\n")

    results = []
    for repeats in heads:
        units = heading_weight_units(nodes, repeats)
        for k1, b in itertools.product(k1s, bs):
            r = BM25Retriever(units, k1=k1, b=b)
            runs = [(r.search(q.question, k=args.k), gold[q.id]) for q in questions]
            m = metrics.evaluate(runs, k=args.k)
            results.append((m["gold_coverage"], m["recall@k"], k1, b, repeats, units))

    results.sort(key=lambda t: (-t[0], -t[1]))
    print(f"{'rank':<5} {'cover':>6} {'recall':>7}  k1    b     heading x")
    print("-" * 46)
    for i, (cov, rec, k1, b, rep, _) in enumerate(results[:8], 1):
        print(f"{i:<5} {cov:>6.3f} {rec:>7.3f}  {k1:<5} {b:<5} {rep}")
    worst = results[-1]
    print(f"{'worst':<5} {worst[0]:>6.3f} {worst[1]:>7.3f}  {worst[2]:<5} {worst[3]:<5} {worst[4]}")

    best_cov, best_rec, bk1, bb, brep, best_units = results[0]
    print(f"\nstrongest baseline: k1={bk1} b={bb} heading x{brep} "
          f"-> coverage {best_cov:.3f} (was 0.733 at defaults k1=1.5 b=0.75 heading x2)")

    # Re-run the ablation against the TUNED baseline.
    retriever = BM25Retriever(best_units, k1=bk1, b=bb)
    base_hits = {q.id: retriever.search(q.question, k=args.k) for q in questions}

    settings = [
        ("tuned BM25, no expansion", args.k, 0, None, graph),
        ("tuned + base 8 d1", 8, 1, 3, graph),
        ("tuned + base 6 d1", 6, 1, 3, graph),
        ("tuned + base 6 d1 both", 6, 1, 3, bigraph),
        ("tuned + base 5 d1 both", 5, 1, None, bigraph),
    ]
    print(f"\n{'setting':<26} {'recall':>7} {'prec':>7} {'covered':>8}")
    print("-" * 52)
    out = {}
    for name, base_n, depth, seeds, g in settings:
        runs = []
        for q in questions:
            ret = expand(base_hits[q.id][:base_n], g, depth=depth, seeds=seeds)[:args.k]
            runs.append((ret, gold[q.id]))
        m = metrics.evaluate(runs, k=args.k)
        out[name] = m
        print(f"{name:<26} {m['recall@k']:>7.3f} {m['precision@k']:>7.3f} "
              f"{m['gold_coverage']:>8.3f}")

    gain = out["tuned + base 6 d1 both"]["gold_coverage"] - \
        out["tuned BM25, no expansion"]["gold_coverage"]
    print(f"\ncoverage gain from expansion over the TUNED baseline: {gain:+.3f} "
          f"({gain*len(questions):.0f} of {len(questions)} questions)")

    dest = config.BENCHMARK.parent / "results_tuned.json"
    dest.write_text(json.dumps({
        "baseline_sweep": {"best": {"k1": bk1, "b": bb, "heading_repeats": brep,
                                    "gold_coverage": best_cov},
                           "worst_gold_coverage": worst[0],
                           "configs_tried": len(results)},
        "ablation": out,
    }, indent=2), encoding="utf-8")
    print(f"-> {dest.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()