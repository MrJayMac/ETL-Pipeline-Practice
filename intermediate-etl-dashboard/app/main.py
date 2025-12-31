from pathlib import Path
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, text

from etl.config import DATABASE_URL, TABLE_SALES, TABLE_DAILY

app = FastAPI(title="ETL Dashboard")

static_dir = Path(__file__).parent / "static"
static_dir.mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}, future=True
    )
else:
    engine = create_engine(DATABASE_URL, future=True)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with engine.connect() as conn:
        daily_rows = conn.execute(
            text(f"SELECT date, revenue FROM {TABLE_DAILY} ORDER BY date")
        ).fetchall()
        top_rows = conn.execute(
            text(
                f"""
                SELECT product,
                       SUM(quantity) AS total_qty,
                       SUM(revenue)  AS total_rev
                FROM {TABLE_SALES}
                GROUP BY product
                ORDER BY total_rev DESC
                LIMIT 5
                """
            )
        ).fetchall()

    labels = [str(r[0]) for r in daily_rows]
    values = [float(r[1]) for r in daily_rows]
    top_products = [
        {"product": r[0], "total_qty": int(r[1]), "total_rev": float(r[2])}
        for r in top_rows
    ]
    chart_json = json.dumps({"labels": labels, "values": values})

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "labels": labels,
            "values": values,
            "top_products": top_products,
            "chart_json": chart_json,
        },
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
