from utils.weather_api import get_coordinates, fetch_weather_data
from utils.data_formatter import print_to_console, save_to_json, save_to_csv
import config


API_KEY = getattr(config, "API_KEY", None)
CITIES = getattr(config, "CITIES", [])
SAVE_CSV = getattr(config, "SAVE_CSV", False)
SAVE_JSON = getattr(config, "SAVE_JSON", False)


def main():

    if not API_KEY:
        print("API key not found.")
        return
    
    if not CITIES:
        print("Please add city or cities.")
        return
    
    all_weather = []
    for city in CITIES:
        coords = get_coordinates(city, API_KEY)
        if coords:
            lat, lon = coords
            weather = fetch_weather_data(lat, lon, API_KEY)
            if weather:
                all_weather.append(weather)

    if all_weather:
        print("\nFormatted Weather Data:\n")
        print_to_console(all_weather)

        if SAVE_CSV:
            save_to_csv(all_weather)

        if SAVE_JSON:
            save_to_json(all_weather)

    return all_weather if SAVE_JSON else None


if __name__ == "__main__":
    main()
