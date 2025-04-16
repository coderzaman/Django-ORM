from django.shortcuts import render, redirect
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

# def home(request):
#    ratings = Rating.objects.defer('restaurant__name').select_related('restaurant')
#    context = {'ratings':ratings}
    
#    return render(request, 'home.html', context)   

from django.db.models import Sum, Prefetch
from django.utils import timezone

# def home(request):
#    # restaurants = Restaurant.objects.prefetch_related('ratings','sales') \
#    #    .filter(ratings__rating=5) \
#    #    .annotate(total=Sum('sales__income'))

#    month_ago = timezone.now() - timezone.timedelta(days=30)

#    monthly_sales = Prefetch(
#       'sales',
#       queryset=Sale.objects.filter(datetime__gte=month_ago)
#    )
#    # restaurants = Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating=5)
#    # restaurants = Restaurant.objects.prefetch_related('ratings','sales').filter(ratings__rating=5, sales__datetime__gte=month_ago)
#    # restaurants = restaurants.annotate(total=Sum('sales__income'))
   
#    # print([r.total for r in restaurants])
#    restaurants = Restaurant.objects.filter(ratings__rating=5, sales__datetime__gte = month_ago ).prefetch_related('ratings', 'sales')
#    print(restaurants)
#    restaurants = Restaurant.objects.filter(ratings__rating=5).prefetch_related('ratings', monthly_sales)
#    print(restaurants)

#    return render(request, 'home.html')   


# def home(request):
   
#    month_ago = timezone.now() - timezone.timedelta(days=30)
   
#    restaurants = Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5, sales__datetime__gte=month_ago).annotate(total=Sum('sales__income'))
#    print([r.total for r in restaurants])
   
#    monthly_sales = Prefetch(
#       'sales',
#       queryset=Sale.objects.filter(datetime__gte=month_ago)
#    )
#    restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5).annotate(total=Sum('sales__income'))
#    print([r.total for r in restaurants])
   
#    restaurants = Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5).annotate(total=Sum('sales__income'))
#    print([r.total for r in restaurants])
   
#    print(restaurants)
   
   
   
#    return render(request, 'home.html')  


# def home(request):
   
#    month_ago = timezone.now() - timezone.timedelta(days=30)
   
#    monthly_sales = Prefetch(
#     'sales',
#     queryset=Sale.objects.filter(datetime__gte=month_ago),
#     to_attr='filtered_sales'  # Store in custom attribute
#    )

#    restaurants = Restaurant.objects.prefetch_related(monthly_sales, 'ratings').filter(ratings__rating=5).annotate(total=Sum('sales__income'))

#    for restaurant in restaurants:
#       print(restaurant.name)
#       print(restaurant.total)
#       for sale in restaurant.filtered_sales:  # Access via custom attribute
#          print(sale.income)

   
   
   
#    return render(request, 'home.html')  

from .models import Staff, StaffRestaurant

def home(request):
   
#    jobs = StaffRestaurant.objects.all()
   
  
#    for job in jobs:
#         print(job.restaurant.name)
#         print(job.staff.name) 

   # Optimize Query Using prefetch related
   
   jobs = StaffRestaurant.objects.prefetch_related('restaurant', 'staff')
   
     
   for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name) 
    
   return render(request, 'home.html')  


from django.shortcuts import render, redirect
from core.forms import ProductOrderForm
from django.db import transaction
from functools import partial
def email_user(email):
     print(f"Dear {email} Thanks for your order")

def order_product(request):
     if request.method == "POST":
         form = ProductOrderForm(request.POST)
         
         if form.is_valid():
              with transaction.atomic():
                    order = form.save()
                    order.product.number_in_stock -= order.number_of_items
                    order.product.save()
              transaction.on_commit(partial(email_user, 'coder.@test.com'))
              return redirect('order_product')
         else:
              context = {'form':form}
              return render(request, 'order.html', context)          
     
     form = ProductOrderForm()
     context = {'form':form}
     return render(request, 'order.html', context)