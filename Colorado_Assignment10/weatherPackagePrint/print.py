# File Name: print.py
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



class WeatherPrinter:
    def display(self, data):
        print("Weather Report")
        print("--------------")
        print("City:", data["City"])
        print("Temperature (Celsius):", data["Temperature (Celsius)"])
        print("Weather:", data["Weather"])
        print("Humidity (%):", data["Humidity (%)"])
        print("Wind Speed (meter/second):", data["Wind Speed (meter/second)"])