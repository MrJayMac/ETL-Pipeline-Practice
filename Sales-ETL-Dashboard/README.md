# Intermediate ETL Pipeline + Dashboard

An intermediate-level ETL pipeline with a simple analytics dashboard.

- ETL: pandas for transforms, SQLAlchemy to load into SQLite
- Dashboard: FastAPI + Jinja2 + Chart.js
- Sample dataset included: `data/raw/sales.csv`

## Project structure

```
Sales-etl-dashboard/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ templates/
│  │  ├─ base.html
│  │  └─ index.html
│  └─ static/
│     └─ css/
│        └─ style.css
├─ etl/
│  ├─ __init__.py
│  ├─ config.py
│  ├─ extract.py
│  ├─ transform.py
│  ├─ load.py
│  └─ pipeline.py
├─ data/
│  ├─ raw/
│  │  └─ sales.csv
│  └─ warehouse/
│     └─ etl.db (generated)
├─ requirements.txt
└─ .env.example
```

## Quickstart

1) Create a virtual environment and install dependencies

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Run the ETL pipeline to populate the SQLite database

```
python -m etl.pipeline
```

3) Start the dashboard

```
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 to view the dashboard.

## Configuration

You can override defaults using environment variables (create a `.env` based on `.env.example`):

- `DATABASE_URL`: SQLAlchemy connection string. Default: `sqlite:///data/warehouse/etl.db`
- `DATA_DIR`: Base data directory. Default: `<project_root>/data`
- `TABLE_SALES`: Sales table name. Default: `sales`
- `TABLE_DAILY`: Daily metrics table name. Default: `daily_metrics`

## Notes

- The ETL reads the sample CSV at `data/raw/sales.csv`, cleans it, computes daily metrics, and loads two tables into SQLite: `sales` and `daily_metrics`.
- The dashboard queries those tables to display daily revenue and top products.
- Modify the CSV or extend the transforms to fit your needs.


# Startup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m etl.pipeline          # populate data/warehouse/etl.db
uvicorn app.main:app --reload   # open http://127.0.0.1:8000