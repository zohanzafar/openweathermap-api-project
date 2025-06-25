import json
import csv
import os


def print_to_console(weather_data):
    for data in weather_data:
        city = data.get("name")
        temp = data.get("main", {}).get("temp")
        desc = data.get("weather", [{}])[0].get("description")
        print(f"{city}: {temp}°C, {desc}")


def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def generate_unique_filename(base_path, base_name, extension):
    filename = f"{base_name}.{extension}"
    full_path = os.path.join(base_path, filename)
    counter = 1

    while os.path.exists(full_path):
        filename = f"{base_name}_{counter}.{extension}"
        full_path = os.path.join(base_path, filename)
        counter += 1

    return full_path


def save_to_csv(weather_data, filename="weather_output"):
    base_path = os.path.join("media", "csv")
    ensure_directory(base_path)

    full_path = generate_unique_filename(base_path, filename, "csv")

    name_tracker = {}
    with open(full_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Temperature (°C)", "Description"])
        for data in weather_data:
            city = data.get("name")
            temp = data.get("main", {}).get("temp")
            desc = data.get("weather", [{}])[0].get("description")

            if city in name_tracker:
                name_tracker[city] += 1
                city_name = f"{city}_{name_tracker[city]}"
            else:
                name_tracker[city] = 0
                city_name = city

            writer.writerow([city_name, temp, desc])

    print(f"\nCSV saved to {full_path}")


def save_to_json(weather_data, filename="weather_output"):
    base_path = os.path.join("media", "json")
    ensure_directory(base_path)

    full_path = generate_unique_filename(base_path, filename, "json")

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(weather_data, f, indent=4)

    print(f"\nJSON saved to {full_path}")
