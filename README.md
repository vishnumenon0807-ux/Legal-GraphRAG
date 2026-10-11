# Legal GraphRAG

Retrieval over Indian regulatory statutes where cross-references between
clauses are graph edges, so finding a clause also pulls in the provisions it
depends on.

Corpus: Companies Act 2013, Akoma Ntoso XML, expression dated **2017-03-28**
(predates the 2017, 2019 and 2020 amendments). Source:
`nyaayaIN/laws-of-india`, `consolidated/The Companies Act, 2013.xml`.

## Setup (Windows)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

If PowerShell blocks activation:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

Open the folder in VS Code and accept the recommended extensions. The
interpreter, `PYTHONPATH`, pytest and ruff-on-save are already configured in
`.vscode/`. F5 runs the stage 1 pipeline.

## Run

```powershell
python scripts\run_pipeline.py        # stage 1: XML -> clauses -> edges -> stats
python scripts\make_candidates.py     # stage 2: build the annotation worklist
python scripts\validate_benchmark.py  # stage 2: check questions.jsonl
pytest                                # 21 tests
```

The Act XML is already in `data/raw/`. Everything under `data/raw/` and
`data/interim/` is gitignored and regenerates in a few seconds;
`data/benchmark/` is committed, because that is the part worth keeping.

## Layout

```
src/legalgraph/
  config.py              paths + corpus registry (add new statutes here)
  parse/
    akoma.py             STAGE 1  done  - XML -> clause nodes
    pdf_statute.py       STAGE 1b stub  - only if the corpus widens
  graph/
    references.py        STAGE 1  done  - typed cross-reference extraction
    stats.py             STAGE 1  done  - connectivity, hubs, multi-hop reach
  benchmark/
    schema.py            STAGE 2  the Question record
    candidates.py        STAGE 2  rank + diversify edges into a worklist
    validate.py          STAGE 2  schema + graph checks on questions.jsonl
  retrieval/
    bm25.py              STAGE 3  stub
    dense.py             STAGE 3  stub
    hybrid.py            STAGE 3  stub  - BM25+dense+rerank, the real baseline
    expand.py            STAGE 4  stub  - graph expansion + ablation
  eval/
    metrics.py           recall@k, precision@k, gold_coverage, by_difficulty
scripts/run_pipeline.py  stage 1 end to end
tests/                   regression tests for the extractor
data/{raw,interim,benchmark}/
```

Clause ids are citation-shaped so a reference resolves to exactly one node:
`s123`, `s123(1)`, `s123(1)(a)`. Once a second instrument joins the graph they
need a corpus prefix (`CA13:s447`); `config.CORPORA` exists for that, and
adding the prefix later means rewriting every id.

## Stage 1 results

| | |
|---|---|
| clause nodes | 3,343 |
| reference mentions | 1,468 |
| clauses with ≥1 reference | 1,032 (36.1%) |
| numbered references resolved | 1,330 / 1,339 (99.3%) |
| traversal edges | 945 |
| edges crossing a section boundary | 359 (38.0%) |
| clauses with a cross-section 2-hop chain | 15 |
| true anaphors needing inference | 22 |

What held: regulatory law is dense enough to be worth traversing. The Indian
Penal Code, checked first, has 0.12 references per section and 6.4% of sections
carrying one. The hubs are the argument: s447 "Punishment for fraud" is
referenced by 14 clauses, s403 "Fee for filing" by 13. Ask what happens when a
company files false incorporation documents and flat retrieval returns s7; the
consequence is in s447, reached only via `s7(7) -> s7(6) -> s447`.

What did not: multi-hop barely exists inside one Act (15 anchors), and the
anaphora-resolution angle is 22 instances. Neither supports a contribution on
this corpus alone.

## Stage 2: the benchmark

Scope decided: **one-hop reference-dependent retrieval over the Companies Act
alone**. Questions whose answer needs a clause that flat retrieval will not
surface, drawn from the 359 cross-section edges. Not multi-hop, because the Act
only supports 15 such chains.

Workflow:

```powershell
python scripts\make_candidates.py     # -> data/benchmark/candidates.md
# work down the file writing questions into data/benchmark/questions.jsonl
python scripts\validate_benchmark.py  # after every session
```

`candidates.md` ranks the 235 usable edges by how hard the target would be for
a retriever that only sees the anchor: mostly lexical dissimilarity between the
two clauses, plus target in-degree and the strength of the governing phrase. A
per-target cap keeps the head of the list varied, since raw score puts nine
s447 edges first and that would produce nine near-identical questions.

`questions.jsonl` ships with 5 worked examples, verified against the clause
text, so the format is unambiguous for a second annotator. Target ~200.

Still needed for a publishable dataset: a second annotator on ~50 questions so
inter-annotator agreement can be reported. That number is the first thing a
reviewer checks to decide whether the labels are trustworthy.

Deferred: widening to the Companies Rules 2014 and SEBI LODR, where genuine
cross-instrument multi-hop structure lives. The schema, graph and metrics all
survive that change, so nothing done now is wasted if it happens later. The
clause ids would need the corpus prefix from `config.CORPORA` at that point.

## Known limitations

- Schedules are detected (15 references) but not parsed or resolved.
- 9 references dangle, mostly into schedules or post-2017 amendments.
- 10 internal clause references are structurally ambiguous: `clause (b)` inside
  s68(4) could be s68(1)(b), (2)(b), (3)(b) or (5)(b). Real ambiguity, flagged
  as `int_clause_ambiguous` rather than guessed.
- The external-Act qualifier can scope over a coordinated list; handled, but
  the heuristic is width-limited.
