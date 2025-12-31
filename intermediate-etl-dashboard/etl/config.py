from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = Path(os.getenv("DATA_DIR", PROJECT_ROOT / "data"))
RAW_DIR = DATA_DIR / "raw"
WAREHOUSE_DIR = DATA_DIR / "warehouse"
RAW_DIR.mkdir(parents=True, exist_ok=True)
WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

# Ensure SQLite path uses POSIX-style separators
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{(WAREHOUSE_DIR / 'etl.db').as_posix()}"
)

TABLE_SALES = os.getenv("TABLE_SALES", "sales")
TABLE_DAILY = os.getenv("TABLE_DAILY", "daily_metrics")
