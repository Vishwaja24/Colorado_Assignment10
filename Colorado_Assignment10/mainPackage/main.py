# File Name: main.py
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

from weatherPackageFetch.fetcher import *
from weatherPackageParser.parser import *
from weatherPackagePrint.print import *
from weatherPackageCSV.writeCSV import WriteCSV

def main():
    print("Denver Weather project")
    api_key = "9bbaaaa1000ccac76e6b0310f8a036ee"
    city = "Denver"

    fetcher = WeatherFetcher("Denver", "9bbaaaa1000ccac76e6b0310f8a036ee")
    raw_data = fetcher.get_weather_data()

    print(raw_data)

    print("===================================================================================") 

    if raw_data:   
        parser = WeatherParser()
        parsed_data = parser.parse(city, raw_data)

        print(parsed_data)
    
    print("===================================================================================") 

    printer = WeatherPrinter()
    printer.display(parsed_data)

    print("===================================================================================") 

    writer = WriteCSV()
    writer.write(parsed_data)



if __name__ == "__main__":
    main()