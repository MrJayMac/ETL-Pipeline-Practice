from .config import RAW_DIR, DATABASE_URL, TABLE_SALES, TABLE_DAILY
from .extract import extract_sales_csv
from .transform import clean_sales, aggregate_daily
from .load import load_to_sqlite


def run() -> None:
    csv_path = RAW_DIR / "sales.csv"
    df = extract_sales_csv(csv_path)
    df_clean = clean_sales(df)
    df_daily = aggregate_daily(df_clean)
    n_sales, n_daily = load_to_sqlite(
        df_clean, df_daily, DATABASE_URL, TABLE_SALES, TABLE_DAILY
    )
    print(
        f"Loaded {n_sales} sales rows and {n_daily} daily metric rows into database: {DATABASE_URL}"
    )


if __name__ == "__main__":
    run()
