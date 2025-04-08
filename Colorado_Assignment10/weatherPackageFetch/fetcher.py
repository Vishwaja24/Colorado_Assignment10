# File Name: fetcher.py
# Student Name: Vishwaja Painjane, Zulqarnayan Hossain, Uruz Bidiwala, Zoha Iqbal
# email:painjavv@mail.uc.edu, hossaizn@mail.uc.edu, bidiwaur@mail.uc.edu, iqbalza@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 10, 2025
# Course #/Section: IS 4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are doing API calls from a weather website collecting weather information on Denver, Colorado.
# Brief Description of what this module does: We continue to build our understanding of API calls and how to use them in Python.
# Citations: openweathermap.org
# Anything else that's relevant: N/A


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