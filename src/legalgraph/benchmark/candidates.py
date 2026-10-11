"""Rank cross-reference edges as benchmark question seeds. STAGE 2 tooling.

The questions themselves are hand-written: that is the contribution. What this
module does is turn 359 edges into a worklist ordered by how much a question
built on each one would actually test retrieval, so annotation starts with the
cases that matter instead of alphabetically.

Scoring signals, in order of weight:

  dissimilarity  1 - Jaccard overlap of content words between source and target.
                 This is the whole point. If the target shares vocabulary with
                 the source, a question phrased from the source will retrieve
                 the target on semantics alone and the edge proves nothing. The
                 interesting edges are the ones where the target reads like a
                 different topic.

  hub            Target in-degree. A provision many clauses depend on is worth
                 more questions than a one-off pointer, and it is the case a
                 practitioner actually hits.

  trigger        Governing phrases that make a reference consequential rather
                 than decorative: "notwithstanding", "subject to",
                 "in contravention of". A bare "under" is usually a citation,
                 not a dependency.

Only cross-section edges are scored. An edge inside one section is already
visible to a baseline that retrieves whole sections, so it cannot support a
question that distinguishes the two systems.
"""

import re
from collections import Counter

STOPWORDS = set(
    "the a an of in to for or and by be is are was were shall may any such this "
    "that with as under not no on at from it its which who whom been has have had "
    "if then than so but all each other than there where when while being do does".split()
)

# phrases that signal the reference changes the rule, not just cites it
STRONG_TRIGGERS = {
    "notwithstanding anything contained in": 1.0,
    "save as otherwise provided in": 0.9,
    "subject to the provisions of": 0.8,
    "without prejudice to": 0.8,
    "in contravention of": 0.8,
    "subject to": 0.7,
    "referred to in": 0.3,
    "in accordance with": 0.3,
    "specified in": 0.25,
    "for the purposes of": 0.2,
}


def content_words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{3,}", text.lower()) if w not in STOPWORDS}


def body(node: dict) -> str:
    return node.get("full_text") or node.get("text") or ""


def cross_section_pairs(nodes: list[dict], edges: list[dict]) -> dict[tuple[str, str], str]:
    """{(src, target): trigger} for edges that leave the source's own section."""
    section_of = {n["id"]: n["section"] for n in nodes}
    pairs: dict[tuple[str, str], str] = {}
    for e in edges:
        if e["kind"] == "self_ref":
            continue
        for target in e["resolved"]:
            if section_of.get(e["src"]) != section_of.get(target):
                # keep the strongest trigger if the pair appears more than once
                prev = pairs.get((e["src"], target), "")
                if STRONG_TRIGGERS.get(e["trigger"], 0) >= STRONG_TRIGGERS.get(prev, 0):
                    pairs[(e["src"], target)] = e["trigger"]
    return pairs


def diversify(rows: list[dict], per_target: int = 3) -> list[dict]:
    """Interleave so no target dominates the head of the worklist.

    Raw score puts nine s447 edges first, which would produce nine near-identical
    questions and a dataset that measures one hub. Keeping the best `per_target`
    edges for each target, then interleaving by rank, spreads the questions over
    distinct provisions without discarding the strong cases.
    """
    buckets: dict[str, list[dict]] = {}
    for r in rows:
        buckets.setdefault(r["target"], []).append(r)

    kept = {t: rs[:per_target] for t, rs in buckets.items()}
    order = sorted(kept.values(), key=lambda rs: -rs[0]["score"])

    out, depth = [], 0
    while any(len(rs) > depth for rs in order):
        for rs in order:
            if len(rs) > depth:
                out.append(rs[depth])
        depth += 1
    return out


def rank(nodes: list[dict], edges: list[dict], min_source_words: int = 12) -> list[dict]:
    by_id = {n["id"]: n for n in nodes}
    pairs = cross_section_pairs(nodes, edges)
    indegree = Counter(t for _, t in pairs)
    max_indegree = max(indegree.values()) if indegree else 1

    out = []
    for (src, target), trigger in pairs.items():
        s_node, t_node = by_id.get(src), by_id.get(target)
        if not s_node or not t_node:
            continue
        sw, tw = content_words(body(s_node)), content_words(body(t_node))
        if len(sw) < min_source_words or not tw:
            # too thin to phrase a question from
            continue

        dissimilarity = 1 - len(sw & tw) / len(sw | tw)
        hub = indegree[target] / max_indegree
        trig = STRONG_TRIGGERS.get(trigger, 0.1)
        score = 0.6 * dissimilarity + 0.25 * hub + 0.15 * trig

        out.append({
            "score": round(score, 4),
            "dissimilarity": round(dissimilarity, 4),
            "target_indegree": indegree[target],
            "trigger": trigger,
            "anchor": src,
            "target": target,
            "anchor_heading": s_node["heading"] or by_id.get(f"s{s_node['section']}", {}).get("heading", ""),
            "target_heading": t_node["heading"] or by_id.get(f"s{t_node['section']}", {}).get("heading", ""),
            "anchor_text": body(s_node)[:300],
            "target_text": body(t_node)[:300],
        })

    out.sort(key=lambda r: -r["score"])
    return out
