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
python scripts\run_pipeline.py     # XML -> clauses -> edges -> stats
pytest                             # 15 regression tests on the extractor
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
    schema.py            STAGE 2  the Question record. Fix before writing q1.
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

Open decision before stage 2: shrink the claim to one-hop reference-dependent
retrieval, or widen the corpus to the Companies Rules 2014 and SEBI LODR, where
cross-instrument references are. The question set depends on which.

## Known limitations

- Schedules are detected (15 references) but not parsed or resolved.
- 9 references dangle, mostly into schedules or post-2017 amendments.
- 10 internal clause references are structurally ambiguous: `clause (b)` inside
  s68(4) could be s68(1)(b), (2)(b), (3)(b) or (5)(b). Real ambiguity, flagged
  as `int_clause_ambiguous` rather than guessed.
- The external-Act qualifier can scope over a coordinated list; handled, but
  the heuristic is width-limited.
