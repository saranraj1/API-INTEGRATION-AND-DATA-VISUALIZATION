from src.api_handler import WeatherAPIHandler
from src.processor import WeatherProcessor
from src.visualizer import WeatherVisualizer

def main():
    cities = ["Coimbatore", "Chennai", "Delhi", "Mumbai", "Bangalore"]
    
    # 1. Fetch
    handler = WeatherAPIHandler()
    raw_results = [handler.fetch_weather(city) for city in cities]
    
    # 2. Process
    processor = WeatherProcessor()
    df = processor.process_weather_data(raw_results)
    
    # 3. Visualize
    visualizer = WeatherVisualizer()
    visualizer.create_dashboard(df)

if __name__ == "__main__":
    main()