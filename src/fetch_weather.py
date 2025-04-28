# fetch_weather.py
import requests
import pandas as pd
from datetime import datetime
import os

# --- Configuration ---
API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API Key
CITY = 'YOUR_CITY'  # Replace with your city name
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# --- Fetching Weather Data ---
response = requests.get(URL)
data = response.json()

# Check if API call was successful
if response.status_code == 200:
    weather = {
        'City': CITY,
        'Temperature (°C)': data['main']['temp'],
        'Humidity (%)': data['main']['humidity'],
        'Pressure (hPa)': data['main']['pressure'],
        'Weather Description': data['weather'][0]['description'],
        'Wind Speed (m/s)': data['wind']['speed'],
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # --- Save to CSV ---
    output_file = 'data/weather_data.csv'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df = pd.DataFrame([weather])

    if os.path.exists(output_file):
        df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        df.to_csv(output_file, index=False)

    print("Weather data saved successfully.")
else:
    print("Failed to fetch data:", data.get('message', 'Unknown error'))