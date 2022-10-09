from django.forms import ModelForm
from .models import Car 

class CreateNewCar(ModelForm): 
    class Meta: 
        model = Car
        fields = ['name', 'category', 'title', 'description', 'year', 'price', 'image']