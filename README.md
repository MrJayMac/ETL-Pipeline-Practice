# ETL-Pipeline-Practice

A collection of ETL (Extract, Transform, Load) pipeline projects for various data processing tasks. This repository serves as a central location for all ETL-related work

## Current Projects

- [COVID-ETL-Pipeline](./COVID-ETL-Pipeline): Processes COVID-19 statistics from public APIs
- [Climate-Trend-ETL](./Climate-Trend-ETL): Processes weather forecast data for climate trend analysis

## Common Technologies

While each project may have specific requirements, common technologies used across projects include:

- Python 3.x
- PostgreSQL (for data storage)
- SQLAlchemy (for database operations)
- Pandas (for data processing)
- Requests (for API interactions)
- python-dotenv (for environment variable management)

## Project Guidelines

- Each ETL project should be self-contained in its own directory
- Use environment variables for sensitive information
- Document all external dependencies in requirements.txt
- Include error handling and logging
- Follow the standard ETL pattern: Extract -> Transform -> Load
- Document the database schema if applicable