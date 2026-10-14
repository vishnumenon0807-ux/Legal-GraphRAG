"""Graph expansion over a base retriever. STAGE 4.

The experiment: take the base retriever's top-k sections, then add the sections
they reference. Everything else is held identical, so any change in the metrics
is attributable to expansion alone.

Two knobs that matter and are both reported:

  depth   how many reference hops to follow. Deeper reaches more but floods the
          context with provisions nobody asked about.

  seeds   how many of the base results to expand from. Expanding from all 10
          pulls in the references of results that were themselves wrong, which
          is the main way expansion hurts precision.

Expanded sections are appended after the base ranking rather than interleaved.
A referenced provision is support for a result, not a competing result, so it
should not displace a base hit from the top of the list.
"""


def expand(
    base: list[str],
    graph: dict[str, set[str]],
    depth: int = 1,
    seeds: int | None = None,
    limit: int | None = None,
) -> list[str]:
    """Base ranking plus referenced sections, in order, no duplicates."""
    if depth <= 0:
        return list(base)

    seed_set = base if seeds is None else base[:seeds]
    seen = set(base)
    out = list(base)

    frontier = list(seed_set)
    for _ in range(depth):
        nxt = []
        for node in frontier:
            for target in sorted(graph.get(node, ())):
                if target not in seen:
                    seen.add(target)
                    out.append(target)
                    nxt.append(target)
        frontier = nxt
        if not frontier:
            break

    return out[:limit] if limit else out


class ExpandedRetriever:
    """Wraps any retriever exposing .search(query, k) -> list[str]."""

    def __init__(self, base, graph, depth=1, seeds=3, base_k=10):
        self.base = base
        self.graph = graph
        self.depth = depth
        self.seeds = seeds
        self.base_k = base_k

    def search(self, query: str, k: int = 10) -> list[str]:
        hits = self.base.search(query, k=self.base_k)
        return expand(hits, self.graph, depth=self.depth, seeds=self.seeds)[:k]
