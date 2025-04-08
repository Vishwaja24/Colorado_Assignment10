#module3.py
#Zulqarnayan

import csv

class WriteCSV:
    def write(self, data, filename='denverWeather_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print("The weather data is written to the CSV file successfully and can be found in the project directory!", filename)




