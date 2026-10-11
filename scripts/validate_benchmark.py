"""Validate the benchmark. Run after every annotation session.

    python scripts/validate_benchmark.py

Exits non-zero if anything is wrong, so it works as a pre-commit check.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from legalgraph import config  # noqa: E402
from legalgraph.benchmark import validate  # noqa: E402


def main():
    nodes = json.loads(config.CLAUSES.read_text(encoding="utf-8"))
    known = {n["id"] for n in nodes}

    questions, parse_errors = validate.load(config.QUESTIONS)
    problems = parse_errors + validate.check(questions, known)

    if problems:
        print(f"{len(problems)} problem(s):\n")
        for p in problems:
            print(f"  {p}")
        print()

    if not questions:
        print("no questions loaded")
        return 1

    stats = validate.summarise(questions, nodes)
    print("summary:")
    for k, v in stats.items():
        print(f"  {k:<30} {v}")

    # the distribution warnings a reviewer would raise
    print()
    if stats["distinct_anchor_sections"] < stats["questions"] * 0.5:
        print("  WARNING: anchors cluster on few sections; the dataset may only test a few hubs")
    if stats["questions"] < 100:
        print(f"  note: {stats['questions']} questions. Inter-annotator agreement on a "
              f"subset needs ~50 double-annotated to be meaningful.")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
