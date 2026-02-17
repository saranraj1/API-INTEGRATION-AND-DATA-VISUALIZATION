import pandas as pd

class WeatherProcessor:
    def process_weather_data(self, data_list):
        """
        Converts a list of API JSON responses into a clean Pandas DataFrame.
        """
        processed_data = []
        
        for entry in data_list:
            if entry:
                # Extracting specific fields from the complex JSON structure
                row = {
                    "City": entry.get("name"),
                    "Temperature": entry.get("main", {}).get("temp"),
                    "Feels_Like": entry.get("main", {}).get("feels_like"),
                    "Humidity": entry.get("main", {}).get("humidity"),
                    "Pressure": entry.get("main", {}).get("pressure"),
                    "Description": entry.get("weather", [{}])[0].get("description"),
                    "Wind_Speed": entry.get("wind", {}).get("speed"),
                    "Cloudiness": entry.get("clouds", {}).get("all")
                }
                processed_data.append(row)
        
        return pd.DataFrame(processed_data)

# Test block
if __name__ == "__main__":
    # Example raw data
    sample_data = [{"name": "Coimbatore", "main": {"temp": 28, "humidity": 60}, "weather": [{"description": "clear sky"}], "wind": {"speed": 3.5}}]
    proc = WeatherProcessor()
    df = proc.process_weather_data(sample_data)
    print(df)