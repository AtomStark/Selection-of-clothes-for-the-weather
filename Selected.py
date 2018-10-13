from GettingTheWeather import selectedWeather
from ApiVK import sendmessage
import configparser
import pickle

conf = configparser.RawConfigParser()
conf.read("config.cfg")

city_id = conf.get("general", "city")
appid = conf.get("general", "appid")
myID = conf.get("general", "user")
access_token = conf.get("general", "access_token")

weather = selectedWeather(city_id,appid)

sendmessage(myID, access_token,weather)

