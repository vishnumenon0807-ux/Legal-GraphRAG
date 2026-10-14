"""Retrieval units and the section-level graph. STAGE 3.

Granularity decision, which everything downstream depends on:

A retriever over a statute returns whole SECTIONS, because that is the unit a
practitioner reads and the unit a citation names. So the corpus is the 471
sections, each indexed on its full text including every subsection and clause.

Two consequences:

  - A gold clause is scored against its containing section. Gold "s137(3)" is
    satisfied by retrieving section 137. This is deliberately generous to the
    baseline: the baseline should be as strong as it honestly can be, or beating
    it proves nothing.

  - Expansion only follows edges that LEAVE the source section. An edge from
    s7(5) to s7(6) adds nothing once section 7 is retrieved whole, which is why
    stage 1 counted cross-section edges separately.
"""

import re
from collections import defaultdict


def section_id(clause_id: str) -> str:
    """s137(3) -> s137 ; s164(1)(g) -> s164 ; s447 -> s447"""
    m = re.match(r"^(s\d+[A-Z]*)", clause_id)
    return m.group(1) if m else clause_id


def build_units(nodes: list[dict]) -> list[dict]:
    """One retrieval unit per section, text = the section's whole subtree."""
    units = []
    for n in nodes:
        if n["type"] != "section":
            continue
        text = n.get("full_text") or n.get("text") or ""
        if not text.strip():
            continue
        heading = n.get("heading", "")
        units.append({
            "id": n["id"],
            "heading": heading,
            # heading repeated once: it is the most topical sentence in the unit
            # and otherwise drowns in a 2,000-word section
            "text": f"{heading}. {heading}. {text}",
            "raw": text,
        })
    return units


def section_graph(nodes: list[dict], edges: list[dict]) -> dict[str, set[str]]:
    """Section -> set of sections it references.

    Collapses the clause-level graph to section level and drops self-loops,
    since an edge inside one section is invisible at this granularity.
    """
    out: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        if e["kind"] == "self_ref":
            continue
        src = section_id(e["src"])
        for target in e["resolved"]:
            tgt = section_id(target)
            if tgt != src:
                out[src].add(tgt)
    return dict(out)


def add_reverse(graph: dict[str, set[str]]) -> dict[str, set[str]]:
    """Make the graph bidirectional.

    Reference direction and question direction do not always agree. s147 ("if
    sections 139 to 146 are contravened, the penalty is...") points AT s139, so
    a question about failing to appoint an auditor retrieves s139 and has to
    follow that edge backwards to find the penalty. Outgoing-only expansion
    cannot do it. Statutes put the consequence in the referencing clause often
    enough that this is a setting worth measuring, not an obvious win: it
    roughly doubles the edges and so the noise.
    """
    both: dict[str, set[str]] = {k: set(v) for k, v in graph.items()}
    for src, targets in graph.items():
        for tgt in targets:
            both.setdefault(tgt, set()).add(src)
    return both


def gold_sections(gold_clauses: list[str]) -> list[str]:
    seen, out = set(), []
    for c in gold_clauses:
        s = section_id(c)
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out
