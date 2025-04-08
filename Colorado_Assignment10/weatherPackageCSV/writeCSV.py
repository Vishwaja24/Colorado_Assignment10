# File Name: WriteCSV.py
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

import csv

class WriteCSV:
    def write(self, data, filename='denverWeather_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print("The weather data is written to the CSV file successfully and can be found in the project directory!", filename)




