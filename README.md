# Weather Data Analysis & Visualization App

This project retrieves real-time weather data for multiple cities using the OpenWeatherMap API, processes the data, and visualizes it in a dashboard comparing Temperature and Humidity.

## Features

- **Data Fetching**: Retrieves real-time weather data (Temperature, Humidity, Wind Speed, Description) for specified cities.
- **Data Processing**: Cleans and structures the API data into a Pandas DataFrame.
- **Data Visualization**: Generates a dashboard with charts for Temperature and Humidity comparison using Matplotlib and Seaborn.
- **Error Handling**: Robust handling for API limitations and network issues.

## Technology Stack

- **Language**: Python 3.x
- **Libraries**:
    - `requests`: For making HTTP requests to the OpenWeatherMap API.
    - `pandas`: For data manipulation and analysis.
    - `matplotlib` & `seaborn`: For creating static visualizations.
    - `python-dotenv`: For managing environment variables (API keys).

## Setup & Installation

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Install Dependencies**:
    Run the following command to install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Key Configuration**:
    - Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api).
    - Create a `.env` file in the root directory.
    - Add your API key to the file:
      ```
      OPENWEATHER_API_KEY=your_actual_api_key_here
      ```

## Usage

Run the main script to fetch data and generate the dashboard:

```bash
python main.py
```

- The script will display a dashboard window.
- It will also save the dashboard image to `output/weather_dashboard.png`.

## Project Structure

- `main.py`: Entry point of the application. Orchestrates fetching, processing, and visualization.
- `src/api_handler.py`: Handles API authentication and data retrieval.
- `src/processor.py`: Parses raw JSON data into a structured DataFrame.
- `src/visualizer.py`: Generates charts and saves the output.
- `notebook/`: Contains Jupyter notebooks for initial exploration.
