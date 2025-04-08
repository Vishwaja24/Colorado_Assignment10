#module1.py
#Uruz
class WeatherPrinter:
    def display(self, data):
        print("Weather Report")
        print("-------------------------")
        print("City:", data["City"])
        print("Temperature (Celsius):", data["Temperature (Celsius)"])
        print("Weather:", data["Weather"])
        print("Humidity (%):", data["Humidity (%)"])
        print("Wind Speed (meter/second):", data["Wind Speed (meter/second)"])