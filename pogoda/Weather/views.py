from django.shortcuts import render
import requests
from .models import City,City2
from .forms import CityForm, CityForm2

def index(request):
    appid = '1a516c056bcd9d98df7e10ca6b794c70'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm

    city = City2.objects.latest('id')

    res = requests.get(url.format(city)).json()
    city_info = {
        'city' : city,
        'temp' : res['main']['temp'],
        'humidity' : res['main']['humidity'],
        'wind' : res['wind']['speed'],
        'icon' : res['weather'][0]['icon']
    }

    context = {'info':city_info, 'form': form}

    return render(request, 'weather/index.html', context)


def info(request):
    appid = '1a516c056bcd9d98df7e10ca6b794c70'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if(request.method == 'POST'):
        form = CityForm2(request.POST)
        form.save()

    form = CityForm2

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city' : city.name,
            'temp' : res['main']['temp'],
            'humidity' : res['main']['humidity'],
            'icon' : res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info':all_cities, 'form':form }

    return render(request, 'weather/info.html', context)