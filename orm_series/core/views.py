from django.shortcuts import render
from .models import Sale, Rating, Restaurant
# Create your views here.

def home(request):
   restaurants = Restaurant.objects.all()
   context = {'restaurants':restaurants}
    
   return render(request, 'home.html', context)   

