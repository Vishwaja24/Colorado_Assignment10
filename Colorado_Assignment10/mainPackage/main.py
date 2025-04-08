#main.py

from weatherPackageFetch.fetcher import *

def main():
    print("Weather project")
    api_key = "9bbaaaa1000ccac76e6b0310f8a036ee"
    city = "Denver"

    fetcher = WeatherFetcher("Denver", "9bbaaaa1000ccac76e6b0310f8a036ee")
    raw_data = fetcher.get_weather_data()

    print(raw_data)






















if __name__ == "__main__":
    main()