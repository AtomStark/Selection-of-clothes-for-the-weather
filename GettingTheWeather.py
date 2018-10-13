import requests

class Weather:
    def __init__(self, temp, conditions, humidity, wind):
        self.list = []
        self.temp = temp
        self.conditions = conditions
        self.humidity = humidity
        self.wind = wind

def selectedWeather(cityID, appid):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': cityID, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        humidity = data['main']['humidity']
        temp = data['main']['temp']
        conditions = data['weather'][0]['description']
        wind = data['wind']['speed']
        weather = Weather(temp, conditions, humidity, wind)
        return weather
    except Exception as e:
        print("Exception (weather):", e)
        pass
