"""Check questions.jsonl against the schema and the graph. STAGE 2.

Annotation errors are silent. A gold clause with a typo'd id just means the
retriever can never score a hit on it, which looks like a weak retriever rather
than a bad label, and you will not notice until the numbers make no sense.
Run this after every annotation session.

Beyond per-record validity it reports the two things a reviewer asks about:
how the questions are distributed across difficulty, and whether the anchors
are spread over the Act or clustered on a handful of provisions.
"""

import json
from collections import Counter
from pathlib import Path

from .schema import Question


def load(path: Path) -> tuple[list[Question], list[str]]:
    """Parse jsonl into Questions. Returns (questions, parse_errors)."""
    questions, errors = [], []
    if not path.exists():
        return [], [f"{path} does not exist"]

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {lineno}: bad JSON ({exc.msg})")
            continue
        try:
            questions.append(Question(**raw))
        except TypeError as exc:
            errors.append(f"line {lineno}: {exc}")
    return questions, errors


def check(questions: list[Question], known_ids: set[str]) -> list[str]:
    problems = []

    seen = Counter(q.id for q in questions)
    for qid, count in seen.items():
        if count > 1:
            problems.append(f"duplicate id {qid} ({count} records)")

    for q in questions:
        problems.extend(q.validate(known_ids))
        if not q.question.strip():
            problems.append(f"{q.id}: empty question")
        if not q.answer.strip():
            problems.append(f"{q.id}: empty answer")
        if not q.annotator:
            problems.append(f"{q.id}: no annotator recorded")
        # a reference_path must start at a gold clause and end at one
        for path in q.reference_path:
            if len(path) < 2:
                problems.append(f"{q.id}: reference_path {path} needs at least two clauses")
                continue
            if path[0] not in q.gold_clauses or path[-1] not in q.gold_clauses:
                problems.append(
                    f"{q.id}: reference_path {path} starts or ends outside gold_clauses"
                )

    return problems


def summarise(questions: list[Question], nodes: list[dict]) -> dict:
    section_of = {n["id"]: n["section"] for n in nodes}
    anchors = [q.anchor_clause for q in questions]
    sections = [section_of.get(a, "?") for a in anchors]
    gold_sizes = [len(q.gold_clauses) for q in questions]

    return {
        "questions": len(questions),
        "by_difficulty": dict(Counter(q.difficulty for q in questions)),
        "by_annotator": dict(Counter(q.annotator for q in questions)),
        "distinct_anchor_clauses": len(set(anchors)),
        "distinct_anchor_sections": len(set(sections)),
        "mean_gold_clauses": round(sum(gold_sizes) / len(gold_sizes), 2) if gold_sizes else 0,
        "most_common_anchor_sections": Counter(sections).most_common(5),
    }
