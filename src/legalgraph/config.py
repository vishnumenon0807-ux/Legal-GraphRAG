"""Paths and corpus registry.

One place to change when you add the Companies Rules 2014 or SEBI LODR, so no
script has a hardcoded filename in it.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
BENCHMARK = DATA / "benchmark"

CLAUSES = INTERIM / "clauses.json"
EDGES = INTERIM / "edges.json"
QUESTIONS = BENCHMARK / "questions.jsonl"

# Each corpus needs a short prefix so clause ids stay unique once more than one
# instrument is in the graph: "CA13:s447" rather than a bare "s447". Add the
# prefix from day one even with a single corpus, or every id changes later.
CORPORA = {
    "CA13": {
        "title": "Companies Act, 2013",
        "expression_date": "2017-03-28",
        "format": "akoma-ntoso",
        "source": RAW / "companies-act-2013.xml",
    },
    # "CR14": {
    #     "title": "Companies (Incorporation) Rules, 2014",
    #     "format": "pdf",
    #     "source": RAW / "companies-rules-2014.pdf",
    # },
}
