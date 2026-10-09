"""Regression tests for the reference extractor.

Every citation form that has already broken once gets a test here. The
extractor is the component the whole project rests on, and its failures are
silent: a missed reference just means a missing edge, which looks like a
correct empty result.
"""

import pytest

from legalgraph.graph.references import MASTER, extract

KINDS = ("chain", "clause_sec", "subsec_sec", "section",
         "int_subsec", "int_clause", "self_ref", "anaphor", "schedule")


def kind_of(text):
    m = MASTER.search(text)
    if not m:
        return None
    for g in KINDS:
        if m.group(g):
            return g
    return None


@pytest.mark.parametrize("text,expected", [
    ("clause (b) of sub-section (1) of section 7", "chain"),
    ("clause (41) of section 2", "clause_sec"),
    ("sub-section (10) of section 143", "subsec_sec"),
    ("in accordance with section 123", "section"),
    ("sections 123 to 127 apply", "section"),
    ("as specified in sub-section (2)", "int_subsec"),
    ("referred to in clause (a)", "int_clause"),
    ("nothing in this section shall apply", "self_ref"),
    ("the provisions of that sub-section", "anaphor"),
    ("Schedule VII", "schedule"),
])
def test_citation_forms(text, expected):
    assert kind_of(text) == expected


def node(nid, section, text, ntype="subsection"):
    return {"id": nid, "type": ntype, "section": section, "num": "1",
            "parent": None, "depth": 1, "heading": "", "text": text,
            "full_text": text}


def test_external_act_is_not_an_internal_edge():
    """'section 5 of the Banking Regulation Act, 1949' must not create an edge
    to this Act's own section 5."""
    nodes = [node("s2(9)", "2", "as defined in clause (c) of section 5 of the "
                                "Banking Regulation Act, 1949"),
             node("s5", "5", "placeholder", "section")]
    edges = extract(nodes)
    assert edges[0]["kind"] == "cross_act"
    assert edges[0]["resolved"] == []


def test_external_qualifier_scopes_over_a_list():
    """'of section 11, sections 11A and 11D of the SEBI Act, 1992' - the
    qualifier governs every item, not just the last."""
    nodes = [node("s24(2)", "24", "powers under sub-sections (1) and (3) of section 11, "
                                  "sections 11A and 11D of the Securities and Exchange "
                                  "Board of India Act, 1992"),
             node("s11", "11", "placeholder", "section")]
    edges = extract(nodes)
    assert edges[0]["kind"] == "cross_act"


def test_ranges_expand():
    nodes = [node("s1(1)", "1", "sections 3 to 6 apply")] + \
            [node(f"s{i}", str(i), "x", "section") for i in (3, 4, 5, 6)]
    edges = extract(nodes)
    assert set(edges[0]["resolved"]) == {"s3", "s4", "s5", "s6"}


def test_self_reference_resolves_to_container():
    nodes = [node("s10(2)", "10", "nothing in this section applies"),
             node("s10", "10", "x", "section")]
    edges = extract(nodes)
    assert edges[0]["kind"] == "self_ref"
    assert edges[0]["resolved"] == ["s10"]


def test_ambiguous_internal_clause_is_flagged_not_guessed():
    """'clause (b)' inside s68(4), where several sibling subsections have a
    clause (b), is genuinely ambiguous and must be reported as such."""
    nodes = [node("s68(4)", "68", "a company referred to in clause (b) shall")] + \
            [node(f"s68({i})(b)", "68", "x", "item") for i in (1, 2, 3)]
    edges = extract(nodes)
    assert edges[0]["kind"] == "int_clause_ambiguous"
    assert len(edges[0]["targets"]) == 3
