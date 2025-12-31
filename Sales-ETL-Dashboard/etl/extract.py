from pathlib import Path
import pandas as pd

def extract_sales_csv(csv_path: Path) -> pd.DataFrame:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV not found at {path}")
    df = pd.read_csv(path)
    return df
