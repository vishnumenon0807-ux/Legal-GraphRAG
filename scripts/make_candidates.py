"""Emit the annotation worklist. STAGE 2.

    python scripts/make_candidates.py             # top 120 to data/benchmark/candidates.md
    python scripts/make_candidates.py --n 300 --jsonl

Work down the markdown file writing questions. Each entry already shows the
anchor clause (what a flat retriever should find), the target it references,
and both texts, so you can judge in a few seconds whether a question is worth
writing without opening the Act.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from legalgraph import config  # noqa: E402
from legalgraph.benchmark import candidates  # noqa: E402


def write_markdown(rows, path, limit):
    lines = [
        "# Annotation worklist",
        "",
        f"Top {min(limit, len(rows))} of {len(rows)} cross-section reference edges, ranked by",
        "how hard the target would be for a retriever that only sees the anchor.",
        "",
        "For each one worth using, write a question whose natural answer needs BOTH",
        "clauses, then add it to `questions.jsonl`. Skip freely: a forced question is",
        "worse than a smaller dataset. Aim for roughly 200 kept.",
        "",
        "---",
        "",
    ]
    for i, r in enumerate(rows[:limit], 1):
        lines += [
            f"## {i}. {r['anchor']} -> {r['target']}",
            "",
            f"score {r['score']} | dissimilarity {r['dissimilarity']} | "
            f"target in-degree {r['target_indegree']} | trigger `{r['trigger'] or 'none'}`",
            "",
            f"**Anchor {r['anchor']}** ({r['anchor_heading'] or 'no heading'})",
            "",
            f"> {r['anchor_text']}",
            "",
            f"**Target {r['target']}** ({r['target_heading'] or 'no heading'})",
            "",
            f"> {r['target_text']}",
            "",
            "```",
            "question:",
            "answer:",
            f"gold_clauses: [\"{r['anchor']}\", \"{r['target']}\"]",
            f"anchor_clause: \"{r['anchor']}\"",
            f"reference_path: [[\"{r['anchor']}\", \"{r['target']}\"]]",
            "difficulty: one_hop",
            "```",
            "",
            "---",
            "",
        ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=120)
    ap.add_argument("--jsonl", action="store_true", help="also write candidates.jsonl")
    ap.add_argument("--per-target", type=int, default=3,
                    help="max edges kept per target clause, to keep the worklist varied")
    args = ap.parse_args()

    nodes = json.loads(config.CLAUSES.read_text(encoding="utf-8"))
    edges = json.loads(config.EDGES.read_text(encoding="utf-8"))
    rows = candidates.diversify(candidates.rank(nodes, edges), per_target=args.per_target)

    config.BENCHMARK.mkdir(parents=True, exist_ok=True)
    md = config.BENCHMARK / "candidates.md"
    write_markdown(rows, md, args.n)
    print(f"{len(rows)} scored candidates -> {md.relative_to(config.ROOT)} (top {args.n})")

    if args.jsonl:
        jl = config.BENCHMARK / "candidates.jsonl"
        jl.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows), encoding="utf-8")
        print(f"full ranking -> {jl.relative_to(config.ROOT)}")

    print("\ntop 10:")
    for r in rows[:10]:
        print(f"  {r['score']:.3f}  {r['anchor']:<14} -> {r['target']:<12} "
              f"{r['target_heading'][:46]}")


if __name__ == "__main__":
    main()
