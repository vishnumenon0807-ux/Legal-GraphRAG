"""Tests for the stage 2 annotation tooling."""

import json
from pathlib import Path

from legalgraph.benchmark import candidates, validate
from legalgraph.benchmark.schema import Question

ROOT = Path(__file__).resolve().parents[1]


def node(nid, section, text, ntype="subsection", heading=""):
    return {"id": nid, "type": ntype, "section": section, "num": "1", "parent": None,
            "depth": 1, "heading": heading, "text": text, "full_text": text}


def test_only_cross_section_edges_are_candidates():
    nodes = [node("s1(1)", "1", "one " * 20), node("s1(2)", "1", "two " * 20),
             node("s9", "9", "nine " * 20, "section")]
    edges = [
        {"src": "s1(1)", "kind": "int_subsec", "surface": "", "trigger": "",
         "targets": ["s1(2)"], "resolved": ["s1(2)"], "ok": True},
        {"src": "s1(1)", "kind": "section", "surface": "", "trigger": "subject to",
         "targets": ["s9"], "resolved": ["s9"], "ok": True},
    ]
    pairs = candidates.cross_section_pairs(nodes, edges)
    assert list(pairs) == [("s1(1)", "s9")]


def test_diversify_breaks_up_a_dominant_target():
    rows = [{"target": "s447", "score": 0.9 - i / 100} for i in range(9)]
    rows += [{"target": "s403", "score": 0.5}]
    out = candidates.diversify(rows, per_target=3)
    assert len(out) == 4                     # 3 x s447 + 1 x s403
    assert out[1]["target"] == "s403"        # second slot is not another s447


def test_validate_catches_unknown_gold_clause():
    q = Question(id="X1", question="q", answer="a", gold_clauses=["s1", "s999"],
                 anchor_clause="s1", annotator="t")
    assert any("s999" in p for p in q.validate({"s1"}))


def test_validate_catches_difficulty_mismatch():
    q = Question(id="X2", question="q", answer="a", gold_clauses=["s1", "s2"],
                 anchor_clause="s1", reference_path=[["s1", "s2"]],
                 difficulty="direct", annotator="t")
    assert any("difficulty" in p for p in q.validate({"s1", "s2"}))


def test_reference_path_must_stay_inside_gold():
    q = Question(id="X3", question="q", answer="a", gold_clauses=["s1", "s2"],
                 anchor_clause="s1", reference_path=[["s1", "s77"]],
                 difficulty="one_hop", annotator="t")
    assert any("outside gold_clauses" in p for p in validate.check([q], {"s1", "s2", "s77"}))


def test_shipped_seed_questions_are_valid():
    """The committed examples must pass, or the format they demonstrate is wrong."""
    nodes = json.loads((ROOT / "data/interim/clauses.json").read_text(encoding="utf-8"))
    questions, errors = validate.load(ROOT / "data/benchmark/questions.jsonl")
    assert not errors
    assert questions
    assert not validate.check(questions, {n["id"] for n in nodes})


def test_expansion_respects_a_fixed_budget():
    """The ablation is only honest if expansion spends slots rather than adding
    them. Expanding a full top-k list and truncating back to k is a no-op, which
    is how the first version of the harness reported 'expansion does nothing'."""
    from legalgraph.retrieval.expand import expand
    graph = {"s1": {"s99"}}
    base = [f"s{i}" for i in range(1, 11)]
    assert expand(base, graph, depth=1)[:10] == base          # no room, no effect
    assert "s99" in expand(base[:5], graph, depth=1)[:10]     # room, takes effect


def test_reverse_edges_reach_the_referencing_section():
    from legalgraph.retrieval import corpus
    both = corpus.add_reverse({"s147": {"s139"}})
    assert both["s139"] == {"s147"}
    assert both["s147"] == {"s139"}


def test_gold_clauses_map_to_their_section():
    from legalgraph.retrieval import corpus
    assert corpus.gold_sections(["s137(3)", "s164(1)(g)", "s447"]) == ["s137", "s164", "s447"]
    assert corpus.section_id("s7(5)") == "s7"
