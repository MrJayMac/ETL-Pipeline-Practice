# News Aggregator ETL Pipeline

## Overview
This project implements an Extract, Transform, Load (ETL) pipeline for news articles from the Wall Street Journal via the News API. It fetches recent articles, processes the data, and loads it into a PostgreSQL database for further analysis.

## Components

### Extract (`extract.py`)
- Connects to the News API
- Retrieves articles from the Wall Street Journal
- Returns the raw JSON data

### Transform (`transform.py`)
- Processes the raw JSON data
- Normalizes the nested JSON structure
- Selects relevant fields (source name, author, title, description, content, URL, publication date)
- Returns a clean pandas DataFrame

### Load (`load.py`)
- Connects to the PostgreSQL database
- Inserts the transformed data into appropriate tables

### Main (`main.py`)
- Orchestrates the ETL process
- Calls extract, transform, and load functions in sequence

## Setup

### Requirements
- Python 3.x
- pandas
- requests
- psycopg2

Install dependencies:
```
pip install -r requirements.txt
```

### Configuration
Create a `.env` file with your API keys and database connection details:
```
NEWS_API_KEY=your_api_key_here
DB_HOST=localhost
DB_NAME=news_db
DB_USER=postgres
DB_PASSWORD=your_password
```

### Database Setup
Create the necessary database tables using the SQL in `database.sql`.

## Usage
Run the ETL pipeline with:
```
python main.py
```

## Notes
- The pipeline handles nested JSON structures from the News API.
- Error handling is included for API and database connection issues.
- The system can be scheduled to run periodically for updated news.