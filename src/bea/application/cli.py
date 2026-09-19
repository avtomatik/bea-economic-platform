import argparse
import logging
from pathlib import Path

from bea.config.paths import DATA_DIR_SRC, DUCKDB_PATH
from bea.ingestion.pipeline import ingest_directory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ingest historical BEA Excel ZIP archives"
    )
    parser.add_argument("--source-dir", type=Path, default=DATA_DIR_SRC)
    parser.add_argument("--db", type=Path, default=DUCKDB_PATH)
    parser.add_argument("--verbose", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    result = ingest_directory(args.source_dir, args.db)
    print(result)


if __name__ == "__main__":
    main()
