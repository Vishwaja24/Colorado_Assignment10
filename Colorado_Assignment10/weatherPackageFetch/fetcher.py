#module2.py
#Vish


import requests

class WeatherFetcher:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.base_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

    def get_weather_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            print("Fetching weather data")
            return response.json()
        else:
            print("Error fetching weather data")
            return None