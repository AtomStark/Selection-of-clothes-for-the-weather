import requests

class Weather:
    def __init__(self, temp, conditions):
        self.list = []
        self.temp = temp
        self.conditions = conditions

def selected(cityID, appid):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': cityID, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        #print("conditions:", data['weather'][0]['description'])
        #print("temp:", data['main']['temp'])
        #print("temp_min:", data['main']['temp_min'])
        #print("temp_max:", data['main']['temp_max'])
        temp = data['main']['temp']
        conditions = data['weather'][0]['description']
        return temp, conditions
    except Exception as e:
        print("Exception (weather):", e)
        pass
