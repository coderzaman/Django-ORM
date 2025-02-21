from core.models import Restaurant, Rating
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint

# def run():
#     restaurants = Restaurant.objects.all()
#     #print(restaurants)
    
#     # python not apply any queries to database to if not it use 
    
#     #then when we run use it it can apply queries to database
    
#     # objects use manager that's means it's mediator between front end and database
#     # It Return a query set that similar to the 
#     print(restaurants)
    
#     print(connection.queries)
    
#     # We can access the list item with index then access it property(db fields value)
#     # print(restaurants[0].name)
    
#     # Return first database objects(row) in db table
#     restaurant = Restaurant.objects.first()
#     print(restaurant.name)
#     print(restaurant.restaurant_type)
#     print(restaurant.date_opened)
#     print(connection.queries)
    
    

# def run():
    
#     # We can creating records with objects(manger) crate function it did not to be save
#     # It return Object of creating records
    
#     restaurant = Restaurant.objects.create(
#         name="Greek Restaurant",
#         date_opened = timezone.now(),
#         restaurant_type = Restaurant.TypeChoices.GREEK,
#         latitude=40.2,
#         longitude=40.5
#     )
    
#     print(restaurant)
#     print(restaurant.restaurant_type)
    
#     print(connection.queries)
    


# def run():
#     # Count the total row in a table
#     print(Restaurant.objects.count())
#     # Access the Last object row item from row
#     print(Restaurant.objects.last())
    
#     print(connection.queries)
    

# def run():
#     user = User.objects.first()
#     restaurant = Restaurant.objects.all()[1]
    
#     if user and restaurant:
#         Rating.objects.create(
#             user=user,
#             restaurant= restaurant,
#             rating = Rating.Rating.NOTBAD,
#         )
        
#         print(Rating.objects.first())
#         print(connection.queries)
        
#     else:
#         print("User or Restaurant Not Found")    
    
        
    
# def run():
#     restaurant = Restaurant.objects.all()[1]
    
#     # Use one parameter like where rating = 1
#     ratings = Rating.objects.filter(rating=1)
#     print(ratings)
    
#     # Use more than one parameter like where rating = 1 OR id = 4 AND OR = restaurant(Object)
#     ratings = Rating.objects.filter(rating=3, id=4, restaurant=restaurant)
#     print(ratings)
    
#     # Use lookup also
#     ratings = Rating.objects.filter(rating__gte=3)
#     print(ratings)
    
#     ratings = Rating.objects.filter(rating__lt=4)
#     print(ratings)
    
#     # Use exclude reverse of filter # Use as WHERE NOT rating >= 3
#     ratings = Rating.objects.exclude(rating__gt=3)
#     print(ratings)
    
#     #we can also use multiple parameter
#     ratings = Rating.objects.exclude(rating__gt=3, restaurant=restaurant)
#     print(ratings)
    
 
 # Updating existing records with model save() method

# def run():
#     restaurant = Restaurant.objects.first()
    
#     restaurant.name = "Something"
    
#     restaurant.save()
    
#     pprint(connection.queries)


# Querying related records in Django ORM
def run():
    rating = Rating.objects.first()
    
    # select related records for restaurant table
    name = rating.restaurant.name
    
    print(name)
    
