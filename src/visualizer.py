import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

class WeatherVisualizer:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_dashboard(self, df):
        """
        Generates and saves a Visualization Dashboard with 6 different metrics.
        """
        if df.empty:
            print("No data available to plot.")
            return

        # Set the visual style
        sns.set_theme(style="whitegrid")
        
        # Create a 2x3 grid of plots
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))
        fig.suptitle('Comprehensive City Weather Analysis Dashboard', fontsize=20, weight='bold')

        # 1. Temperature
        sns.barplot(x="City", y="Temperature", data=df, ax=axes[0, 0], palette="coolwarm")
        axes[0, 0].set_title("Temperature (°C)")
        axes[0, 0].set_ylabel("Temp (°C)")

        # 2. Feels Like Temperature
        sns.barplot(x="City", y="Feels_Like", data=df, ax=axes[0, 1], palette="husl")
        axes[0, 1].set_title("Feels Like Temperature (°C)")
        axes[0, 1].set_ylabel("Temp (°C)")

        # 3. Humidity
        sns.barplot(x="City", y="Humidity", data=df, ax=axes[0, 2], palette="Blues")
        axes[0, 2].set_title("Humidity Levels (%)")
        axes[0, 2].set_ylabel("Humidity (%)")

        # 4. Pressure
        sns.barplot(x="City", y="Pressure", data=df, ax=axes[1, 0], palette="Greens")
        axes[1, 0].set_title("Atmospheric Pressure (hPa)")
        axes[1, 0].set_ylabel("Pressure (hPa)")
        # Zoom in on pressure since it varies little (around 1000)
        min_pressure = df["Pressure"].min() - 10 if not df["Pressure"].empty else 900
        axes[1, 0].set_ylim(bottom=min_pressure)

        # 5. Wind Speed
        sns.barplot(x="City", y="Wind_Speed", data=df, ax=axes[1, 1], palette="viridis")
        axes[1, 1].set_title("Wind Speed (m/s)")
        axes[1, 1].set_ylabel("Speed (m/s)")

        # 6. Cloudiness
        sns.barplot(x="City", y="Cloudiness", data=df, ax=axes[1, 2], palette="Greys")
        axes[1, 2].set_title("Cloudiness (%)")
        axes[1, 2].set_ylabel("Cloud Cover (%)")

        # Layout adjustment and saving
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        output_path = os.path.join(self.output_dir, "weather_dashboard.png")
        plt.savefig(output_path)
        print(f"Dashboard saved successfully to {output_path}")
        plt.show()

if __name__ == "__main__":
    # Test with dummy DataFrame having all fields
    test_df = pd.DataFrame({
        "City": ["Coimbatore", "Chennai", "Bangalore", "Delhi", "Mumbai"],
        "Temperature": [30, 34, 24, 40, 32],
        "Feels_Like": [32, 38, 24, 42, 35],
        "Humidity": [65, 80, 50, 30, 75],
        "Pressure": [1012, 1008, 1015, 1005, 1010],
        "Wind_Speed": [3.5, 5.2, 4.1, 2.5, 6.0],
        "Cloudiness": [20, 10, 40, 0, 50]
    })
    viz = WeatherVisualizer()
    viz.create_dashboard(test_df)