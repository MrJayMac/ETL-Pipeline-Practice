import requests

def extract_data(bbox=None):
    base_url = 'https://opensky-network.org/api/states/all'
    
    if bbox:
        lamin, lomin, lamax, lomax = bbox
        url = f"{base_url}?lamin={lamin}&lomin={lomin}&lamax={lamax}&lomax={lomax}"
    else:
        url = base_url

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Fetched data successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
