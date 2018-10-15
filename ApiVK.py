import requests

def sendmessage(user_id, access_token, weather, tshirts, outerwear):
    temperature_msg = 'Температура: ' + str(weather.temperature) + '. '
    conditions_msg = 'Облачность: ' + weather.conditions + '. '
    humidity_msg = 'Влажность: ' + str(weather.humidity) + '. '
    wind_msg = 'Скорость ветра: ' + str(weather.wind) + '. \n'
    clothes = "Стоить одеть футболку: " + tshirts + ". \n" + outerwear
    message = temperature_msg + conditions_msg + humidity_msg + wind_msg + clothes
    url = "https://api.vk.com/method/"
    send = 'messages.send?user_id=' + user_id + '&message=' + message + '&v=5.52&access_token='
    req = dict(requests.get(url + send + access_token).json())
    answer = str(req)
    if answer.__contains__("error"):
        print("ERROR :")
        error = req.get("error")
        print(error.get("error_msg"))
        exit()
    print(message)
