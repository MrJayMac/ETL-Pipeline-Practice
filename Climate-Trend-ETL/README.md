# Climate-Trend-ETL

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for climate data focused on New York City. It retrieves a 7-day weather forecast including maximum temperature, minimum temperature, and precipitation data, processes it, and stores it in a PostgreSQL database for analysis.

## Features

- **Extract**: Fetches climate data from the Open-Meteo API
- **Transform**: Cleans and structures the data for analysis
- **Load**: Stores the processed data in a PostgreSQL database
- **Environment Variables**: Uses .env file for secure database connection

## Project Structure

```
Climate-Trend-ETL/
├── extract.py      # Handles data extraction from Open-Meteo API
├── transform.py    # Processes and transforms the raw data
├── load.py         # Loads transformed data into PostgreSQL
├── main.py         # Main script that orchestrates the ETL process
├── metrics.sql     # SQL schema for the metrics table
└── requirement.txt # Project dependencies
```

## Requirements

- Python 3.x
- PostgreSQL database
- Python packages:
  - requests
  - pandas
  - sqlalchemy
  - python-dotenv

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Climate-Trend-ETL.git
   cd Climate-Trend-ETL
   ```

2. Install the required packages:
   ```
   pip install requests pandas sqlalchemy python-dotenv
   ```

3. Set up your PostgreSQL database and create a `.env` file with your database connection string:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   ```

## Usage

Run the ETL pipeline with:

```
python main.py
```

This will:
1. Extract weather forecast data from Open-Meteo API for New York City
2. Transform the data into a structured format
3. Load the data into the PostgreSQL database in the `metrics` table

## Database Schema

The data is stored in a table called `metrics` with the following structure:

```sql
CREATE TABLE metrics (
    time DATE,          -- Date of the forecast
    tempmax FLOAT,      -- Maximum temperature in °C
    tempmin FLOAT,      -- Minimum temperature in °C
    totalrainfall FLOAT -- Precipitation sum in mm
);
```

## Customization

To change the location for weather data, modify the latitude and longitude parameters in `extract.py`.
