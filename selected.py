from GettingTheWeather import selected
from GettingTheWeather import Weather

city_id = 524311
appid = ""

weather = Weather(selected(city_id,appid)[0], selected(city_id,appid)[1])

print(weather.conditions)
print(weather.temp)
