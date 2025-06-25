import requests


def get_coordinates(city, api_key):
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    try:
        response = requests.get(geo_url, params={"q": city, "limit": 1, "appid": api_key})
        response.raise_for_status()
        data = response.json()
        if not data:
            print(f"Could not find coordinates for {city}")
            return None
        return data[0]["lat"], data[0]["lon"]
    except requests.exceptions.RequestException as err:
        print(f"Error getting coordinates for {city}: {err}")
        return None


def fetch_weather_data(lat, lon, api_key):
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(weather_url, params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error fetching weather data: {err}")
        return None
