import pandas as pd


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    if 'quantity' in df.columns:
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    if 'unit_price' in df.columns:
        df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)
    if 'revenue' not in df.columns and {'quantity', 'unit_price'}.issubset(df.columns):
        df['revenue'] = df['quantity'] * df['unit_price']

    # Drop rows with invalid dates
    df = df.dropna(subset=['date'])
    return df


def aggregate_daily(df: pd.DataFrame) -> pd.DataFrame:
    dfd = df.copy()
    dfd['date'] = pd.to_datetime(dfd['date'])
    daily = (
        dfd.groupby(dfd['date'].dt.date)
           .agg(revenue=('revenue', 'sum'), quantity=('quantity', 'sum'))
           .reset_index(names='date')
    )
    return daily
