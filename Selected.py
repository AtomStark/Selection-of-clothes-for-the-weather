from GettingTheWeather import selectedWeather
from ApiVK import sendmessage

from BD import user_get, get_Сlothes, create_outerwear_table
import configparser

from service import select_outerwear

conf = configparser.RawConfigParser()
conf.read("config.cfg")

user = user_get("'Anton'")
city_id = int(user.city_id)
user_id = user.user_id.rstrip()
yesterdays_color = user.yesterdays_color
app_id = conf.get("general", "app_id")
access_token = conf.get("general", "access_token")

weather = selectedWeather(city_id, app_id)
tshirts = get_Сlothes("tshirts", yesterdays_color)
outerwear = select_outerwear(weather.temperature)

sendmessage(user_id, access_token, weather, tshirts, outerwear)
