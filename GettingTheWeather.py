import requests

class Weather:
    def __init__(self, temperature, conditions, humidity, wind):
        self.list = []
        self.temperature = temperature
        self.conditions = conditions
        self.humidity = humidity
        self.wind = wind

def selectedWeather(city_id, app_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        humidity = data['main']['humidity']
        temperature = data['main']['temp']
        conditions = data['weather'][0]['description']
        wind = data['wind']['speed']
        weather = Weather(temperature, conditions, humidity, wind)
        return weather
    except Exception as e:
        print("Exception (weather):", e)
        pass
