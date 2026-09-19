from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR_SRC = BASE_DIR / "data" / "external"
DATA_DIR_WRH = BASE_DIR / "data" / "warehouse"
DUCKDB_PATH = DATA_DIR_WRH / "bea.duckdb"
