========================
Weather Report Generator
========================

This project helps you check the weather in different cities and saves the results in clean files (CSV and JSON). The files can be used later for reports or analysis.

-------------------------
What Does It Do?
-------------------------

- Looks up each city from a list.
- Finds the location (latitude and longitude).
- Gets the current weather (temperature and description).
- Shows the results on screen (Console).
- Saves the results to:
  - A CSV file 
  - A JSON file 

You can choose whether you want to save files or just see the results.

-------------------------
Before You Start
-------------------------

Make sure you have:

1. Python installed on your computer (version 3.6 or higher).
2. An internet connection (needed to fetch weather data).
3. An API Key from OpenWeather (https://openweathermap.org/api).

-------------------------
How to Set It Up (Step by Step)
-------------------------

1. Download the Project

   Save it anywhere on your computer.

2. Create a Virtual Environment (Recommended)

   This helps keep your project’s dependencies separate from other projects.

   ▶ On **Windows**:

       python -m venv venv
       venv\Scripts\activate

   ⚠️ Note for PowerShell Users on **Windows**:
       If you see an error like running scripts is disabled on this system when trying to activate the virtual environment, PowerShell is blocking script execution.

   You can fix it temporarily (only for the current session) by running this command in the same PowerShell window:

       Set-ExecutionPolicy Unrestricted -Scope Process  

   Then activate the virtual environment again:

       venv\Scripts\activate

   ▶ On **Ubuntu/Linux**:

       python3 -m venv venv
       source venv/bin/activate

3. Install Python Modules

   After activating the virtual environment, run:

       pip install -r requirements.txt

   (Note: If requirements.txt is not available, install manually by running:
   pip install requests python-dotenv)

4. Add Your API Key

   Create a file named .env in the main folder. Add this line in it:

       OPENWEATHER_API_KEY=your_api_key_here

   Replace `your_api_key_here` with the key you got from the OpenWeather website.

5. Set Cities and File Options

   Open the file config.py.

   - Add the cities you want to check here:

         CITIES = ["London", "New York", "Tokyo", "Delhi"]

   - To save as CSV or JSON, set these to True:

         SAVE_JSON = True
         SAVE_CSV = True

   - If you don’t want to save files, set them to False.

-------------------------
How to Run the Project
-------------------------

Once everything is ready, run the main script:

   python main.py

You’ll see the weather results printed on the screen.

If file saving is turned on, you'll find the saved files in these folders:

- media/json/ → for JSON files
- media/csv/ → for CSV files

Each time you run the project, it creates a new file with a unique name so nothing is overwritten.

-------------------------
Example Output
-------------------------

On the screen:

   London: 18°C, light rain
   New York: 25°C, clear sky
   Tokyo: 21°C, scattered clouds
   Delhi: 33°C, haze

In CSV:

   | City   | Temperature (°C) | Description      |
   |--------|------------------|------------------|
   | London | 18               | light rain       |
   | Tokyo  | 21               | scattered clouds |

In JSON:

   [
     {
       "name": "London",
       "main": { "temp": 18 },
       "weather": [{ "description": "light rain" }]
     }
   ]

-------------------------
Notes
-------------------------

- If a city is not found or the internet is not working, it will show a message.
- You can add or remove cities any time in the config.py file.
- The project does not store any personal information.

