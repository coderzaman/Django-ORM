from django.shortcuts import render
from .forms import RestaurantForm
# Create your views here.

def home(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, None)
        
        if form.is_valid():
            print(form.cleaned_data) #clean data return a dictionary fields and value fair
        else:
            return render(request, 'home.html', context={'form':form}) 
        
    return render(request, 'home.html', context={'form':RestaurantForm()})   

