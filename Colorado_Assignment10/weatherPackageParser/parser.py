#module4.py
#Zoha
class WeatherParser:
    def parse(self, city, data):
        try:
            return {
                "City": city,
                "Temperature (Celsius)": data["main"]["temp"],
                "Weather": data["weather"][0]["description"],
                "Humidity (%)": data["main"]["humidity"],
                "Wind Speed (meter/second)": data["wind"]["speed"]
            }
        except (KeyError, TypeError) as e:
            print(f" Error in parsing data: {e}")
            return None