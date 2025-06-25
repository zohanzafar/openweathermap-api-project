import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITIES = ["London", "New York", "Tokyo", "Delhi"]

# If set True, will save the JSON data in json file. By default set to False.
SAVE_JSON = True

# If set True, will save the data in csv file. By default is set to False.
SAVE_CSV = True
