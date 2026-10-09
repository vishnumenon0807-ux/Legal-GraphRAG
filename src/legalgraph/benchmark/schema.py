"""The benchmark record format. STAGE 2 - the actual contribution.

Fix this before writing question one. Changing the schema after 200 questions
means re-annotating all of them.

The field that makes this dataset worth publishing is `gold_clauses`: the set a
retriever MUST return for the question to be answerable. Without it you cannot
tell a retrieval failure from a generation failure, which is the whole point.

`reference_path` records HOW each non-obvious gold clause is reached, so you can
report results split by hop count and show that the hard cases are hard.
"""

from dataclasses import asdict, dataclass, field
from typing import Literal

Difficulty = Literal["direct", "one_hop", "multi_hop"]


@dataclass
class Question:
    id: str                       # "CA13-017"
    question: str
    answer: str                   # short free text, for the generation stage
    gold_clauses: list[str]       # every clause needed; order irrelevant
    anchor_clause: str            # the one a flat retriever should plausibly find
    reference_path: list[list[str]] = field(default_factory=list)
    # e.g. [["s7(7)", "s7(6)", "s447"]] - how a non-anchor gold clause is reached
    difficulty: Difficulty = "direct"
    annotator: str = ""
    notes: str = ""

    def validate(self, known_ids: set[str]) -> list[str]:
        problems = []
        if self.anchor_clause not in self.gold_clauses:
            problems.append(f"{self.id}: anchor not listed in gold_clauses")
        for c in self.gold_clauses:
            if c not in known_ids:
                problems.append(f"{self.id}: gold clause {c} not in graph")
        hops = max((len(p) - 1 for p in self.reference_path), default=0)
        expected = {0: "direct", 1: "one_hop"}.get(hops, "multi_hop")
        if self.difficulty != expected:
            problems.append(
                f"{self.id}: difficulty={self.difficulty} but longest path implies {expected}"
            )
        if len(self.gold_clauses) == 1 and self.difficulty != "direct":
            problems.append(f"{self.id}: single gold clause cannot be {self.difficulty}")
        return problems

    def to_json(self) -> dict:
        return asdict(self)


# Worked example. Keep one real record in the schema file so the format is never
# ambiguous to a second annotator.
EXAMPLE = Question(
    id="CA13-001",
    question="What is the consequence if a company furnishes false information "
             "in its application for incorporation?",
    answer="The persons responsible are liable for fraud under section 447.",
    gold_clauses=["s7(5)", "s7(6)", "s447"],
    anchor_clause="s7(5)",
    reference_path=[["s7(5)", "s447"], ["s7(6)", "s447"]],
    difficulty="one_hop",
    annotator="vm",
    notes="s447 is unreachable by semantic similarity from the question wording.",
)
