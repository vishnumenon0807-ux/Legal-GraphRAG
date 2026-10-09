"""Stage 1 end to end: XML -> clauses -> edges -> stats.

    python scripts/run_pipeline.py
    python scripts/run_pipeline.py --source path/to/act.xml
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from legalgraph import config  # noqa: E402
from legalgraph.graph import references, stats  # noqa: E402
from legalgraph.parse import akoma  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=None, help="statute XML (default: config.CORPORA CA13)")
    ap.add_argument("--skip-stats", action="store_true")
    args = ap.parse_args()

    src = Path(args.source) if args.source else config.CORPORA["CA13"]["source"]
    if not src.exists():
        raise SystemExit(
            f"source not found: {src}\n"
            "Put the statute XML in data/raw/ (see README) or pass --source."
        )

    config.INTERIM.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] parsing {src.name}")
    nodes = akoma.parse(str(src))
    config.CLAUSES.write_text(json.dumps(nodes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"      {len(nodes)} clause nodes -> {config.CLAUSES.relative_to(config.ROOT)}")

    print("[2/3] extracting cross-references")
    edges = references.extract(nodes)
    config.EDGES.write_text(json.dumps(edges, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"      {len(edges)} mentions -> {config.EDGES.relative_to(config.ROOT)}")
    references.report(nodes, edges)

    if not args.skip_stats:
        print("\n[3/3] graph statistics")
        sys.argv = ["stats", str(config.CLAUSES), str(config.EDGES)]
        stats.main()


if __name__ == "__main__":
    main()
