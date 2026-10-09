"""Graph-level viability check.

Usage: python3 -I src/graph_stats.py data/clauses.json data/edges.json

The question this answers: if a retriever finds the right clause and then walks
the reference edges, how much extra does it pull in, and how many clauses sit
far enough down a chain that a flat retriever would never reach them?

A multi-hop question is only possible where a clause's reference target itself
references something else. Counting those is what tells you whether a multi-hop
benchmark can be built on this corpus at all.
"""

import json
import sys
from collections import Counter, defaultdict, deque

SELF_KINDS = {"self_ref"}


def build(nodes, edges):
    ids = {n["id"] for n in nodes}
    out = defaultdict(set)
    for e in edges:
        if e["kind"] in SELF_KINDS:
            continue
        for t in e["resolved"]:
            # an edge into your own ancestor or descendant is structure, not a
            # cross-reference; it adds nothing a hierarchical retriever lacks
            if t == e["src"] or t.startswith(e["src"]) or e["src"].startswith(t):
                continue
            if t in ids:
                out[e["src"]].add(t)
    return out


def expand(out, start, hops):
    seen = {start}
    frontier = {start}
    for _ in range(hops):
        nxt = set()
        for u in frontier:
            nxt |= out.get(u, set()) - seen
        seen |= nxt
        frontier = nxt
        if not frontier:
            break
    return seen - {start}


def main():
    nodes = json.load(open(sys.argv[1], encoding="utf-8"))
    edges = json.load(open(sys.argv[2], encoding="utf-8"))
    out = build(nodes, edges)

    n_edges = sum(len(v) for v in out.values())
    sources = [n for n in nodes if n["id"] in out]
    indeg = Counter(t for v in out.values() for t in v)

    print(f"nodes: {len(nodes)}   traversal edges: {n_edges}")
    print(f"clauses with >=1 outgoing reference: {len(out)} "
          f"({100*len(out)/len(nodes):.1f}%)")
    print(f"clauses referenced by something else: {len(indeg)} "
          f"({100*len(indeg)/len(nodes):.1f}%)")
    print()

    print("most-referenced clauses (the hubs a flat retriever keeps missing):")
    byid = {n["id"]: n for n in nodes}
    for cid, c in indeg.most_common(10):
        node = byid.get(cid, {})
        label = node.get("heading") or (node.get("text") or "")[:58]
        print(f"  {cid:<14} in={c:<4} {label[:58]}")
    print()

    # how much does traversal add, for clauses that have any reference at all
    one = [len(expand(out, n["id"], 1)) for n in sources]
    two = [len(expand(out, n["id"], 2)) for n in sources]
    three = [len(expand(out, n["id"], 3)) for n in sources]
    print("expansion from a clause that has references:")
    print(f"  1 hop : mean {sum(one)/len(one):.2f}  max {max(one)}")
    print(f"  2 hops: mean {sum(two)/len(two):.2f}  max {max(two)}")
    print(f"  3 hops: mean {sum(three)/len(three):.2f}  max {max(three)}")
    print()

    # the benchmark-viability number
    multi = [n["id"] for n in sources
             if len(expand(out, n["id"], 2)) > len(expand(out, n["id"], 1))]
    print(f"clauses where hop 2 reaches something hop 1 does not: {len(multi)}")
    print(f"  -> that many clauses can anchor a genuine multi-hop question")
    deep = [c for c in multi if len(expand(out, c, 3)) > len(expand(out, c, 2))]
    print(f"clauses that still gain at hop 3: {len(deep)}")
    print()

    # A retriever normally returns the whole section, so an edge that stays
    # inside the source's own section is already visible to a flat baseline.
    # Only edges that LEAVE the section can justify graph traversal.
    sec_of = {n["id"]: n["section"] for n in nodes}
    cross = {(u, v) for u, vs in out.items() for v in vs
             if sec_of.get(u) != sec_of.get(v)}
    print(f"edges that cross a section boundary: {len(cross)} of {n_edges} "
          f"({100*len(cross)/n_edges:.1f}%)")

    xout = defaultdict(set)
    for u, v in cross:
        xout[u].add(v)
    xmulti = []
    for cid in xout:
        h1 = xout[cid]
        if any(xout.get(a, set()) - h1 - {cid} for a in h1):
            xmulti.append(cid)
    print(f"clauses with a genuine CROSS-SECTION 2-hop chain: {len(xmulti)}")
    print()

    print("sample cross-section 2-hop chains:")
    printed = 0
    for cid in sorted(xmulti):
        h1 = xout[cid]
        done = False
        for a in sorted(h1):
            for b in sorted(xout.get(a, set()) - h1 - {cid}):
                ha = (byid.get(b, {}).get("heading")
                      or (byid.get(b, {}).get("text") or "")[:44])
                print(f"  {cid} -> {a} -> {b:<12} [{ha[:44]}]")
                printed += 1
                done = True
                break
            if done:
                break
        if printed >= 8:
            break


if __name__ == "__main__":
    main()
