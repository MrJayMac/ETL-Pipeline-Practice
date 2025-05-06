import os
from dotenv import load_dotenv
import requests

def extract_data():

    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None