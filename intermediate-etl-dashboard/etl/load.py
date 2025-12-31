from typing import Tuple

import pandas as pd
from sqlalchemy import create_engine


def load_to_sqlite(
    df_sales: pd.DataFrame,
    df_daily: pd.DataFrame,
    db_url: str,
    table_sales: str = "sales",
    table_daily: str = "daily_metrics",
) -> Tuple[int, int]:
    engine = create_engine(db_url, future=True)
    df_sales.to_sql(table_sales, con=engine, if_exists='replace', index=False)
    df_daily.to_sql(table_daily, con=engine, if_exists='replace', index=False)
    return len(df_sales), len(df_daily)
