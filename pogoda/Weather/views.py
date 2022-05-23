from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = '1a516c056bcd9d98df7e10ca6b794c70'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(City.name)).json()
        city_info = {
            'city' : City.name,
            'temp' : res['main']['temp'],
            'icon' : res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'info':city_info}

    return render(request, 'weather/index.html', context)