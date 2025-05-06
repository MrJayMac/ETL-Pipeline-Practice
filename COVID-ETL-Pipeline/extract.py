import requests

def extract_data():

    url = 'https://disease.sh/v3/covid-19/countries'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Extract successful")
        return data
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None