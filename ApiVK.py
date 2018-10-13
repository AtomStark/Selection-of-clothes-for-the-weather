import requests

def sendmessage(userID, access_token, weather):
    tempMsg = 'Температура: ' + str(weather.temp) + '. '
    conditionsMsg = 'Облачность: ' + weather.conditions + '. '
    humidityMsg = 'Влажность: ' + str(weather.humidity) + '. '
    windMsg = 'Скорость ветра: ' + str(weather.wind)
    message = tempMsg + conditionsMsg + humidityMsg + windMsg
    url = "https://api.vk.com/method/"
    send = 'messages.send?user_id=' + userID + '&message=' + message + '&v=5.52&access_token='
    req = requests.get(url + send + access_token).json()
    print(message)
