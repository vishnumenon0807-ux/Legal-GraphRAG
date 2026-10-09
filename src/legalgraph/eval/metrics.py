"""Retrieval metrics. STAGE 3/4.

Deliberately small. The headline number for this project is gold_coverage:
the fraction of questions where EVERY required clause was retrieved. Mean
recall hides the failure that matters, because a question answered from two of
its three required clauses is still answered wrong.
"""


def recall_at_k(retrieved: list[str], gold: list[str], k: int) -> float:
    if not gold:
        return 1.0
    top = set(retrieved[:k])
    return len(top & set(gold)) / len(gold)


def precision_at_k(retrieved: list[str], gold: list[str], k: int) -> float:
    top = retrieved[:k]
    if not top:
        return 0.0
    return len(set(top) & set(gold)) / len(top)


def fully_covered(retrieved: list[str], gold: list[str], k: int) -> bool:
    """Every gold clause present in the top k. The strict, honest metric."""
    return set(gold).issubset(set(retrieved[:k]))


def evaluate(runs: list[tuple[list[str], list[str]]], k: int = 10) -> dict:
    """runs: [(retrieved_ids, gold_ids), ...] for every question."""
    if not runs:
        return {}
    n = len(runs)
    return {
        "n": n,
        "k": k,
        "recall@k": sum(recall_at_k(r, g, k) for r, g in runs) / n,
        "precision@k": sum(precision_at_k(r, g, k) for r, g in runs) / n,
        "gold_coverage": sum(fully_covered(r, g, k) for r, g in runs) / n,
    }


def by_difficulty(runs_with_meta: list[tuple[list[str], list[str], str]], k: int = 10) -> dict:
    """Same metrics split by question difficulty. Report this, not just the
    aggregate: a system can look fine overall while failing every multi-hop
    question, and that split is the interesting result."""
    buckets: dict[str, list[tuple[list[str], list[str]]]] = {}
    for retrieved, gold, diff in runs_with_meta:
        buckets.setdefault(diff, []).append((retrieved, gold))
    return {d: evaluate(rs, k) for d, rs in sorted(buckets.items())}
