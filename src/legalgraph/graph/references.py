"""Extract cross-reference edges from parsed clause nodes.

Usage: python3 -I src/extract_refs.py data/clauses.json data/edges.json

Every reference mention found in a clause's own text becomes one record. The
point of this script is not just to build edges but to MEASURE how many
references are mechanically resolvable, because that number decides whether
the anaphoric cases are worth a research contribution.

Reference kinds:
  chain        clause (a) of sub-section (1) of section 2   -> fully specified
  clause_sec   clause (41) of section 2
  subsec_sec   sub-section (2) of section 123
  section      section 123 / sections 123 to 127
  int_subsec   sub-section (2)        -> same section
  int_clause   clause (a)             -> same subsection
  anaphoric    this section / the said section / the foregoing
  cross_act    section 466 of the Companies Act, 1956
  schedule     Schedule VII
"""

import json
import re
import sys
from collections import Counter

SEC = r"\d+[A-Z]*"
SUB = r"\d+[A-Z]?"
CL = r"[a-z]{1,3}|[ivx]{1,5}|\d{1,3}"

MASTER = re.compile(
    rf"""
    (?P<chain>clause\s*\((?P<ch_cl>{CL})\)\s*of\s*sub-?section\s*\((?P<ch_ss>{SUB})\)\s*of\s*section\s*(?P<ch_sec>{SEC}))
  | (?P<clause_sec>clause\s*\((?P<cs_cl>{CL})\)\s*of\s*section\s*(?P<cs_sec>{SEC}))
  | (?P<subsec_sec>sub-?sections?\s*(?P<ss_list>\(\s*{SUB}\s*\)(?:\s*(?:,|and|or|to)\s*\(\s*{SUB}\s*\))*)\s*of\s*section\s*(?P<ss_sec>{SEC}))
  | (?P<section>sections?\s*(?P<sec_list>{SEC}(?:\s*(?:,|and|or|to)\s*{SEC})*))
  | (?P<int_subsec>sub-?sections?\s*(?P<is_list>\(\s*{SUB}\s*\)(?:\s*(?:,|and|or|to)\s*\(\s*{SUB}\s*\))*))
  | (?P<int_clause>clauses?\s*\((?P<ic_cl>{CL})\))
  | (?P<self_ref>this\s+(?P<sr_unit>sub-?section|section|clause|Chapter|Part))
  | (?P<anaphor>the\s+said\s+(?:sub-?section|section|clause)
       | that\s+sub-?section
       | the\s+(?:aforesaid|foregoing)
       | the\s+preceding\s+sub-?section)
  | (?P<schedule>(?:the\s+)?(?:First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|Eleventh)\s+Schedule
       | Schedule\s+[IVX]+)
    """,
    re.VERBOSE | re.IGNORECASE,
)

# "... of the Companies Act, 1956" following a reference means it points out of
# this corpus. A bare "of this Act" does not. The qualifier may sit after a
# coordinated list of further section numbers, as in "sub-sections (1) and (2)
# of section 11, sections 11A and 11D of the SEBI Act, 1992" -- where the
# qualifier scopes over every item in the list, not just the last.
EXTERNAL = re.compile(
    r"\s*(?:\s*(?:,|and|or)?\s*(?:sections?\s+)?\d+[A-Z]*)*\s*"
    r"of\s+the\s+[^.;:]{0,80}?Act,\s*(\d{4})",
    re.IGNORECASE,
)

TRIGGERS = [
    "notwithstanding anything contained in",
    "save as otherwise provided in",
    "without prejudice to",
    "subject to the provisions of",
    "subject to",
    "in accordance with",
    "referred to in",
    "specified in",
    "provided in",
    "provided under",
    "for the purposes of",
    "within the meaning of",
    "prescribed under",
    "in contravention of",
    "in pursuance of",
    "under",
]


def expand(tokens, is_sub=False):
    """'123, 124 and 127' -> ['123','124','127']; '123 to 126' -> range."""
    raw = re.findall(r"\d+[A-Z]?" if is_sub else r"\d+[A-Z]*", tokens)
    if re.search(r"\bto\b", tokens, re.I) and len(raw) == 2:
        a, b = raw
        if a.isdigit() and b.isdigit() and int(b) - int(a) < 60:
            return [str(n) for n in range(int(a), int(b) + 1)]
    return raw


def find_trigger(text, start):
    """The governing phrase must sit immediately before the reference. A loose
    'appears somewhere nearby' test makes 'under' swallow everything."""
    window = text[max(0, start - 45):start].lower().rstrip()
    for t in TRIGGERS:
        if window.endswith(t):
            return t
    return ""


def parent_id(cid):
    """Drop the LAST component: s123(1)(a) -> s123(1);  s123(1) -> s123"""
    m = re.match(r"^(.*)\(\w+\)$", cid)
    return m.group(1) if m else cid


def extract(nodes):
    ids = {n["id"] for n in nodes}
    by_section = {}
    for n in nodes:
        by_section.setdefault(n["section"], []).append(n["id"])
    edges = []

    for n in nodes:
        text = n["text"]
        if not text:
            continue
        sec = n["section"]

        for m in MASTER.finditer(text):
            kind = m.lastgroup
            for g in ("chain", "clause_sec", "subsec_sec", "section",
                      "int_subsec", "int_clause", "self_ref", "anaphor",
                      "schedule"):  # most specific first; kind may be revised below
                if m.group(g):
                    kind = g
                    break

            surface = m.group(0)
            tail = text[m.end():m.end() + 90]
            ext = EXTERNAL.match(tail)
            targets = []

            if ext and kind in ("chain", "clause_sec", "subsec_sec", "section"):
                kind = "cross_act"
            elif kind == "chain":
                targets = [f"s{m.group('ch_sec')}({m.group('ch_ss')})({m.group('ch_cl')})"]
            elif kind == "clause_sec":
                targets = [f"s{m.group('cs_sec')}({m.group('cs_cl')})"]
            elif kind == "subsec_sec":
                targets = [f"s{m.group('ss_sec')}({s})"
                           for s in expand(m.group("ss_list"), is_sub=True)]
            elif kind == "section":
                targets = [f"s{s}" for s in expand(m.group("sec_list"))]
            elif kind == "int_subsec":
                targets = [f"s{sec}({s})" for s in expand(m.group("is_list"), is_sub=True)]
            elif kind == "int_clause":
                # "clause (b)" with no governing section. Try the unit the
                # sentence sits in, then its parent. If neither has such a
                # clause the reference crosses to another subsection of the
                # same section and the text does not say which -- that is a
                # genuine scope ambiguity, not a parsing failure.
                cl = m.group("ic_cl")
                targets = []
                for base in (n["id"], parent_id(n["id"])):
                    cand = f"{base}({cl})"
                    if cand in ids:
                        targets = [cand]
                        break
                if not targets:
                    sibs = [c for c in by_section.get(sec, []) if c.endswith(f"({cl})")]
                    if len(sibs) == 1:
                        targets = sibs
                    elif len(sibs) > 1:
                        kind = "int_clause_ambiguous"
                        targets = sibs
                    else:
                        targets = [f"{parent_id(n['id'])}({cl})"]
            elif kind == "self_ref":
                unit = re.sub(r"[^a-z]", "", m.group("sr_unit").lower())
                if unit == "section":
                    targets = [f"s{sec}"]
                elif unit == "subsection":
                    targets = [n["id"] if n["type"] == "subsection" else parent_id(n["id"])]
                elif unit == "clause":
                    targets = [n["id"]]

            resolved = [t for t in targets if t in ids]
            edges.append({
                "src": n["id"],
                "kind": kind,
                "surface": surface,
                "trigger": find_trigger(text, m.start()),
                "targets": targets,
                "resolved": resolved,
                "ok": bool(resolved) or (kind in ("anaphor", "cross_act", "schedule")),
            })

    return edges


def report(nodes, edges):
    n_nodes = len(nodes)
    with_text = sum(1 for n in nodes if n["text"])
    kinds = Counter(e["kind"] for e in edges)
    resolvable = [e for e in edges if e["targets"]]
    hit = [e for e in resolvable if e["resolved"]]
    srcs = len({e["src"] for e in edges})
    pairs = {(e["src"], t) for e in edges for t in e["resolved"]}

    print(f"nodes: {n_nodes}  (with own text: {with_text})")
    print(f"reference mentions: {len(edges)}")
    print(f"clauses containing >=1 reference: {srcs} ({100*srcs/with_text:.1f}% of text-bearing)")
    print(f"mentions per text-bearing clause: {len(edges)/with_text:.2f}")
    print(f"distinct resolved edges: {len(pairs)}")
    print()
    print("by kind:")
    for k, c in kinds.most_common():
        print(f"  {k:<12} {c:>5}  ({100*c/len(edges):4.1f}%)")
    print()
    print(f"numeric targets attempted: {len(resolvable)}")
    print(f"  resolved to a real node: {len(hit)} ({100*len(hit)/max(1,len(resolvable)):.1f}%)")
    print(f"  dangling:                {len(resolvable)-len(hit)}")
    print()

    # Edges that actually add something at retrieval time. A self_ref points at
    # the unit the reader is already looking at, so it buys nothing.
    trav = {(e["src"], t) for e in edges if e["kind"] != "self_ref" for t in e["resolved"]}
    outside = {(s, t) for s, t in trav if not (t.startswith(s) or s.startswith(t))}
    print(f"traversable edges (excl. self-reference): {len(trav)}")
    print(f"  of which leave the source's own subtree: {len(outside)}")
    print(f"self-reference mentions ('this section' etc): {kinds['self_ref']}")
    print(f"true anaphors (need inference, not regex):   {kinds['anaphor']}"
          f"  ({100*kinds['anaphor']/len(edges):.1f}% of mentions)")
    print()
    print("top triggers:")
    for t, c in Counter(e["trigger"] for e in edges if e["trigger"]).most_common(8):
        print(f"  {t:<36} {c}")


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    nodes = json.load(open(sys.argv[1], encoding="utf-8"))
    edges = extract(nodes)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(edges, f, ensure_ascii=False, indent=1)
    report(nodes, edges)


if __name__ == "__main__":
    main()
