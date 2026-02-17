import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class WeatherAPIHandler:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

        if not self.api_key:
            raise ValueError("API Key not found. Please check your .env file.")

    def fetch_weather(self, city_name):
        """
        Fetches current weather data for a specific city.
        """
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'  # Gets temperature in Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 401:
                print("Error: Invalid API Key. Please check your .env file.")
            elif response.status_code == 404:
                print(f"Error: City '{city_name}' not found.")
            else:
                print(f"HTTP Error processing request for {city_name}: {http_err}")
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"Connection Error: {e}")
            return None

# Quick test block
if __name__ == "__main__":
    handler = WeatherAPIHandler()
    test_city = "Coimbatore"  
    data = handler.fetch_weather(test_city)
    
    if data:
        print(f"Successfully fetched data for {test_city}!")
        print(f"Current Temp: {data['main']['temp']}°C")