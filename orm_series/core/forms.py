from django import forms
from .models import Restaurant, Rating, Sale

from django.core.validators import MinValueValidator, MaxValueValidator


# we can use validator also in form 
from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")  # Only including the relevant fields