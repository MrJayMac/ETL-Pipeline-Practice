# COVID-19 ETL Pipeline

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-14+-blue.svg)](https://www.postgresql.org/download/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An end-to-end ETL (Extract, Transform, Load) pipeline that automates the process of collecting, processing, and storing COVID-19 statistics from a public API into a PostgreSQL database.

## 🚀 Project Overview

This pipeline automates the following workflow:

- **Extract**: Pulls live COVID-19 data for all countries from the [disease.sh API](https://disease.sh/docs/)
- **Transform**: Cleans and processes the data, including:
  - Selecting key columns (country, cases, deaths, recoveries, timestamp)
  - Converting timestamp into human-readable datetime
  - Data validation and cleaning
- **Load**: Inserts the processed data into a local PostgreSQL database in a table named `covid_stats`

## 📦 Tech Stack

- **Python 3.8+**
- **PostgreSQL 14+**
- **SQLAlchemy** - Database ORM
- **Pandas** - Data processing and analysis
- **Requests** - HTTP requests handling
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL 14 or higher
- pip (Python package manager)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MrJayMac/COVID-ETL-Pipeline.git
   cd COVID-ETL-Pipeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

3. Set up PostgreSQL:
   - Install PostgreSQL if not already installed
   - Create a new database named `covid`
   - Create a user with appropriate permissions

4. Configure environment variables:
   - Create a `.env` file in the project root
   - Add your database connection string:
     ```
     DATABASE_URL=postgresql://username:password@localhost:5432/covid
     ```

## 🚀 Usage

Run the pipeline:
```bash
python main.py
```

The pipeline will:
1. Extract data from the disease.sh API
2. Transform the data into a clean format
3. Load the data into your PostgreSQL database

## 📊 Database Schema

The pipeline creates a table named `covid_stats` with the following schema:
- country (VARCHAR)
- cases (INTEGER)
- deaths (INTEGER)
- recoveries (INTEGER)
- last_update (TIMESTAMP)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Your Name - [Your Email](mailto:your.email@example.com)

Project Link: [https://github.com/MrJayMac/COVID-ETL-Pipeline](https://github.com/MrJayMac/COVID-ETL-Pipeline)

## 🔗 Links

- [disease.sh API Documentation](https://disease.sh/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python Documentation](https://docs.python.org/3/)

---

Made with ❤️ by [Your Name](https://github.com/MrJayMac)
