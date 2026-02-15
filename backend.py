import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather_data(city):
    """
    Fetches 5-day forecast data + City Coordinates.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # NEW: We return a dictionary with TWO pieces of info now:
        # 1. The City data (lat, lon, name)
        # 2. The Forecast list (temps, rain, etc)
        return {
            "city": data["city"], 
            "forecast": data["list"]
        }
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    print("Testing backend...")
    test_city = "London"
    result = get_weather_data(test_city)
    if result:
        print(f"Success! Found city: {result['city']['name']}")
        print(f"Coordinates: {result['city']['coord']}")
    else:
        print("Failed to get data.")