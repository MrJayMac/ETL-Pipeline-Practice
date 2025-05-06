import os
from dotenv import load_dotenv
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    load_dotenv()
    database = os.getenv('DATABASE_URL')

    raw_data = extract_data()
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data, database)


if __name__ == "__main__":
    main()