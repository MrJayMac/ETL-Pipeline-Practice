import requests

def extract_data():
    url = 'https://api.open-meteo.com/v1/forecast'
    # Coordinates for New York City
    params = {
        'latitude': 40.7128,
        'longitude': -74.0060,
        'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum',
        'timezone': 'auto',
        'forecast_days': 7  # Get forecast for 7 days
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        print('Extract successful')
        return data
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
