from .models import City, City2
from django.forms import ModelForm, TextInput, widgets

class CityForm(ModelForm):
    class Meta:
        model = City2
        fields = ['name']
        widgets = {'name':TextInput(attrs={'class':
            'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
            })}