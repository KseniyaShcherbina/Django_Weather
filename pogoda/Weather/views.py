from django.shortcuts import render
import requests

def index(request):
    appid = '1a516c056bcd9d98df7e10ca6b794c70'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city))
    print(res.text)

    return render(request, 'weather/index.html')

