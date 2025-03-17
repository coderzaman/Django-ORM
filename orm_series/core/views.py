from django.shortcuts import render
from .models import Sale, Rating, Restaurant
# Create your views here.

# def home(request):
#    restaurants = Restaurant.objects.prefetch_related('ratings',  'sales')
#    context = {'restaurants':restaurants}
    
#    return render(request, 'home.html', context)   

# def home(request):
#    ratings = Rating.objects.only('rating','restaurant__name', 'user__username').select_related('restaurant','user')
#    context = {'ratings':ratings}
    
#    return render(request, 'home.html', context)   


# def home(request):
#    ratings = Rating.objects.only('rating','restaurant__name','user__username', 'user__username').select_related('restaurant','user')
#    context = {'ratings':ratings}
    
#    return render(request, 'home.html', context)   

def home(request):
   ratings = Rating.objects.defer('restaurant__name').select_related('restaurant')
   context = {'ratings':ratings}
    
   return render(request, 'home.html', context)   
