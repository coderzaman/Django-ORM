from core.models import Restaurant, Rating, Sale, Staff
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
# def run():
#     rating = Rating.objects.first()
    
#     # select related records for restaurant table
#     name = rating.restaurant.name
    
#     print(name)
    

# Querying reverse relations in Django
# def run():
    # restaurant = Restaurant.objects.first()
    
    #print(restaurant.rating_set.all())    
    
    # You can override the FOO_set name by setting the related_name parameter in the ForeignKey definition.
    # print(restaurant.ratings.all())
    
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 30.34,
    #     datetime = timezone.now(),
    # )
    
     
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 20.34,
    #     datetime = timezone.now(),
    # )
    
     
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.last(),
    #     income = 40.34,
    #     datetime = timezone.now(),
    # )
    
     
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.last(),
    #     income = 50.34,
    #     datetime = timezone.now(),
    # )
    
    # print(Restaurant.objects.first().sales.all())


# Getting OR creating data with Model.objects.get_or_create()

# def run():
#     restaurant = Restaurant.objects.last()
#     user = User.objects.last()
    
    # print(Rating.objects.get_or_create(
    #    user = user,
    #    restaurant = restaurant,
    #    rating = Rating.Rating.WORST 
    # )) 
    
    # pprint(connection.queries)
    
    # this execute four if not data exist in db
    # First: restaurant = Restaurant.objects.last()
    # Second: user = User.objects.last()
    # Third: Select the row if exist(Check of each individual with AND)
    # Four: True Then execute Insert query if false not execute the insert query 
    
    # get_or_create  return a tuple
    
    # rating, created = Rating.objects.get_or_create(
    #    user = user,
    #    restaurant = restaurant,
    #    rating = Rating.Rating.WORST)

    # print(created) # It should be false
    # pprint(connection.queries) # Now execute three queries expect insert
    
    # # We can Apply some operation 
    
    # if created:
    #     print("Some things here")

# def run():
#     restaurant = Restaurant.objects.last()
#     user = User.objects.last()
    
#     Rating.objects.create(
#         user = user,
#         restaurant = restaurant,
#         rating = 9 # Is assign value to database because of validator are not validate in database level
#         # It validate on Model form
#     )
    
#     rating =  Rating(user = user, restaurant = restaurant, rating = 9)
    
#     rating.full_clean() # Now validator add to the raise the validation errors. Because validate added to the field 
    
    
    
#     rating.save()
    

# Update individual Records

# def run():
#     restaurant = Restaurant()
    
#     restaurant.name = "Bangladeshi Restaurant 2"
#     restaurant.restaurant_type = Restaurant.TypeChoices.BANGLADESHI
#     restaurant.date_opened = timezone.now()
#     restaurant.latitude = 90.3
#     restaurant.longitude = 123.4
    
    # restaurant = Restaurant.objects.first()
    
    # restaurant.name = "New Restaurant"
    # restaurant.save(update_fields=['name', 'website'])
    
    # pprint(connection.queries)


# Update all the date_opened time to now

# def run():
#     # restaurant = Restaurant.objects.all()
    
#     restaurant = Restaurant.objects.filter(name__startswith="P")
   
#     restaurant.update(
#         date_opened = timezone.now() - timezone.timedelta(365),
#         # We can change multiple field with update field
#         website='https://test.com'
#     )
    
#     pprint(connection.queries)

# Deleting model instances with model delete() function

# def run():
#     restaurant  = Restaurant.objects.first()
    
#     print(restaurant.delete())
    
#     pprint(connection.queries)


# def run():
#     Restaurant.objects.create(
#         name = "Bangladeshi Restaurant",
#         restaurant_type = Restaurant.TypeChoices.BANGLADESHI,
#         date_opened = timezone.now(),
#         latitude = 90.34,
#         longitude = 130.42,
#     )
    
#     Restaurant.objects.create(
#         name = "Chinese Restaurant",
#         restaurant_type = Restaurant.TypeChoices.CHINESE,
#         date_opened = timezone.now(),
#         latitude = 91.34,
#         longitude = 120.42,
#     )
     
#     Restaurant.objects.create(
#         name = "Italian Restaurant",
#         restaurant_type = Restaurant.TypeChoices.ITALIAN,
#         date_opened = timezone.now(),
#         latitude = 190.34,
#         longitude = 123.42,
#     )
#     Restaurant.objects.create(
#         name = "Greek Restaurant",
#         restaurant_type = Restaurant.TypeChoices.GREEK,
#         date_opened = timezone.now(),
#         latitude = 190.34,
#         longitude = 134.42,
#     )
    
#     Restaurant.objects.create(
#         name = "Fast Food",
#         restaurant_type = Restaurant.TypeChoices.FASTFOOD,
#         date_opened = timezone.now(),
#         latitude = 97.34,
#         longitude = 170.42,
#     )

# Django QuerySet delete() method to remove multiple objects


# def run():
    
#     print(Restaurant.objects.all().delete())
    
#     pprint(connection.queries)


# Filtering QuerySets with filter() method 


# def run():
#     # Filter return a query set where have no object of records
#     print(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.BANGLADESHI))
    
#     restaurant = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.BANGLADESHI)
    
#     # count function return no item in query set
#     print(restaurant.count())
    
#     pprint(connection.queries)


# Getting a single model back with the get() method

# def run():
#     restaurant = Restaurant.objects.get(name="Pizzeria 1")
    
#     # If restaurant found it return only this record object
#     print(restaurant)

# def run():
#     restaurant = Restaurant.objects.get(name="Something Wrong")
    
#     # If Record is not found it Raise error
#     print(restaurant)


# exist function
# def run():
#     restaurant = Restaurant.objects.filter(name="Something Wrong")
    
#     # Returns False if the QuerySet is empty
#     print(restaurant.exists())  
    
#     # Returns True if the QuerySet contains at least one record
#     restaurant = Restaurant.objects.filter(name="Pizzeria 1")
#     print(restaurant.exists())

# Multiple AND conditions with the filter() method
# def run(): 
#     chinese = Restaurant.TypeChoices.CHINESE
    
#     # Applying multiple filter conditions (AND logic)
#     restaurants = Restaurant.objects.filter(restaurant_type=chinese, name__startswith="C")
    
#     print(restaurants)

# # Filtering QuerySets with the “in” lookup
# def run():
#     chinese = Restaurant.TypeChoices.CHINESE
#     italian = Restaurant.TypeChoices.ITALIAN
#     bangladeshi = Restaurant.TypeChoices.BANGLADESHI
    
#     check_types = [chinese, bangladeshi,italian]
    
#     # `in` lookup takes a list or tuple
#     restaurants = Restaurant.objects.filter(
#         restaurant_type__in=check_types
#     )
    
#     print(restaurants)

# Filtering QuerySets with the exclude() method

# def run():
#     chinese = Restaurant.TypeChoices.CHINESE
    
#     # Exclude all records where restaurant_type is CHINESE
#     restaurants = Restaurant.objects.exclude(restaurant_type=chinese)
#     print(restaurants)
    
#     # Exclude records where restaurant_type is CHINESE and name starts with "C"
#     restaurants = Restaurant.objects.exclude(restaurant_type=chinese, name__startswith="C")
#     print(restaurants)


# Filtering QuerySets with “lt” and “gt” lookups
# def run():
#     # Fetch restaurants where the name starts with A, B, C, D (less than 'E')
#     restaurants = Restaurant.objects.filter(name__lt='E')
#     print(restaurants)

#     # Fetch restaurants where latitude is less than 80
#     restaurants = Restaurant.objects.filter(latitude__lt=80)
#     print(restaurants)

#     # Fetch sales records where income is greater than or equal to 50
#     sales = Sale.objects.filter(income__gte=50)
#     print(sales)

# Filtering QuerySets with the range lookup
# It like Between in SQL
# def run():
#     # Fetch sales records where income is between 50 and 60 (inclusive)
#     sales = Sale.objects.filter(income__range=(50, 60))

#     # Print income values from the filtered results
#     print([sales.income for sales in sales])

#     # Display executed SQL queries
#     pprint(connection.queries)

# Ordering QuerySets with the order_by() method
# def run():
#     # Order restaurants by name in ascending order (A-Z)
#     restaurant = Restaurant.objects.order_by('name')
#     print(restaurant)
    
#     # Order restaurants by name in descending order (Z-A)
#     restaurant = Restaurant.objects.order_by('-name')
#     print(restaurant) 
    
#     # Reverse an already ordered QuerySet (alternative to using '-')
#     restaurant = Restaurant.objects.order_by('name').reverse()
#     print(restaurant) 
    
#     # Ordering can be applied to text, numeric, and datetime fields.
    
#     # Order sales by most recent datetime (latest sales first)
#     sales = Sale.objects.order_by('-datetime') 
    
#     for sale in sales:
#         print(sale.datetime)
    
#     # Print executed queries
#     pprint(connection.queries)

#Case-Insensitive Orderings with the Lower Database Function
# from django.db.models.functions import Lower

# def run():
#     # Order restaurant names case-insensitively
#     restaurants = Restaurant.objects.order_by(Lower('name'))
#     print(restaurants)
    
#     # Print executed queries
#     pprint(connection.queries)
    
    
# Indexing and Slicing into QuerySets - LIMIT and OFFSET SQL statement

# def run():
#     # Retrieve the 5th restaurant (index 4, zero-based index)
#     restaurants = Restaurant.objects.order_by('name')[4]
#     print(restaurants)
    
#     # Retrieve the first 4 restaurants
#     restaurants = Restaurant.objects.order_by('name')[:4]
#     print(restaurants)
    
#     # Retrieve restaurants from index 4 to the end
#     restaurants = Restaurant.objects.order_by('name')[4:]
#     print(restaurants)
    
#     # Retrieve restaurants from index 2 to 5 (excluding index 5)
#     restaurants = Restaurant.objects.order_by('name')[2:5]
#     print(restaurants)
    
#     # **Negative indexing is not supported:**
#     # restaurants = Restaurant.objects.order_by('name')[-4:]

# Adding ‘ordering’ field to model Meta class for default ordering
# def run():
#     restaurants = Restaurant.objects.all();
#     print(restaurants)
    
#     pprint(connection.queries)


#  earliest() and latest() functions
# def run():
#     # Fetch the earliest restaurant based on latitude (smallest latitude value)
#     restaurant = Restaurant.objects.earliest('latitude')
#     print(restaurant)

#     # Fetch the earliest restaurant in descending order (largest latitude value)
#     restaurant = Restaurant.objects.earliest('-latitude')
#     print(restaurant)

# def run():
#     # Fetch the latest restaurant based on date opened
#     restaurant = Restaurant.objects.latest('date_opened')
#     print(restaurant)



# # Effect of get_latest_by:
# def run():
#     # Fetch the latest restaurant based on the default get_latest_by field (date_opened)
#     restaurant = Restaurant.objects.latest()
#     print(restaurant)

#     # You can still override the field manually
#     restaurant = Restaurant.objects.latest('website')
#     print(restaurant)


# # Filtering by foreign key values

# def run():
#     #find all rating associated with a restaurant beginning with B
    
#     ratings = Rating.objects.filter(restaurant__name__startswith='B') 
#     print(ratings)
    
#     # It execute inner join in sql
#     pprint(connection.queries)
    
#     # let see another example it return all sales of bangladeshi restaurant
#     bangladeshi = Restaurant.TypeChoices.BANGLADESHI
    
#     sales = Sale.objects.filter(restaurant__restaurant_type = bangladeshi)
#     print(sales)

# def run():
#     # Create an Staff
#     staff, created = Staff.objects.get_or_create(name="John Wick")
#     print(staff)
#     print(type(staff.restaurants)) # This object type is ManyRelatedManager. It is used handle many to many relationship in django
    
#     # Check Staff has any associated restaurant
#     print(staff.restaurants.all()) # <QuerySet []> because we not associate any restaurant with staff 
    
#     # Create relationship or associate 
#     staff.restaurants.add(Restaurant.objects.first())
#     print(staff.restaurants.all())
    
#     #<QuerySet []>
#     #<QuerySet [<Restaurant: Pizzeria 1>]>
    
#     # If we see on junction table it create association with staff and restaurant with their pk
    
#     # count(): No of associated entries
#     print(staff.restaurants.count()) #1
    
#     # remove: Remove an association
#     staff.restaurants.remove(Restaurant.objects.first())
#     print(staff.restaurants.count()) #0
    
#     # set: create multiple association 
#     staff.restaurants.set(Restaurant.objects.all()[:5])
#     print(staff.restaurants.count()) #5
    
#     # clear: Remove all association
#     staff.restaurants.clear()
#     print(staff.restaurants.count()) #0
    
#     #filter: filter associate table data
#     staff.restaurants.set(Restaurant.objects.all()[:5])
#     italian = staff.restaurants.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
#     print(italian) #<QuerySet [<Restaurant: Pizzeria 1>, <Restaurant: Pizzeria 2>]>
    
#     # We can access other side of object with _set
#     restaurant = Restaurant.objects.get(pk=25)
#     print(restaurant.staff_set.all()) #<QuerySet [<Staff: John Wick>]>
    
#     # we can  also use here  add, remove, set, clear
#     staff, created = Staff.objects.get_or_create(name="Vin Den")
#     restaurant.staff_set.add(staff)
    
#     restaurant = Restaurant.objects.get(pk=30)
#     restaurant.staff_set.set(Staff.objects.all())
#     restaurant.staff_set.clear()

from core.models import StaffRestaurant
# import random

# def run():
#     staff, created = Staff.objects.get_or_create(name="John Wick")
#     restaurant = Restaurant.objects.first()
#     restaurant2 = Restaurant.objects.last()
    
#     # Create Function
#     StaffRestaurant.objects.create(
#         staff=staff, restaurant=restaurant,salary=300000
#     )
    
#     StaffRestaurant.objects.create(
#         staff=staff, restaurant=restaurant2,salary=400000
#     )
    
#     #clear function
#     # staff.restaurants.clear()
#     staff, created = Staff.objects.get_or_create(name="John Wick")
    
#     #add Function
#     staff.restaurants.add(Restaurant.objects.first(), through_defaults={'salary':20_000})
    
#     # other filled ith through_default Which take an dictionary
#     staff.restaurants.clear()
    
#     #set function
#     staff.restaurants.set(
#         Restaurant.objects.all()[:10],
#         through_defaults={'salary':random.randint(20_000, 80_000)})
    
#     # remove function
#     restaurant = Restaurant.objects.first()
#     staff.restaurants.remove(restaurant)
    

from django.db.models.functions import Upper
    
# def run():
#     #Values 
#     restaurants = Restaurant.objects.values('name', 'date_opened')
#     print(restaurants)     
    
#     # See query how query are execute in backend 
#     pprint(connection.queries)
    
    
#     # we can get only first, last or part item from it
#     restaurant = Restaurant.objects.values('name').first()
#     print(restaurant['name'])
#     restaurant = Restaurant.objects.values('name').last()
#     print(restaurant['name'])
    
#     # Get first five item
#     restaurants = Restaurant.objects.values(name_upper=Upper('name'))[:5]
#     print(restaurants)
    
#     for restaurant in restaurants:
#         print(restaurant["name_upper"])
    
    
#     # Getting Foreign Key data with values() function
#     ratings = Rating.objects.values('rating','restaurant__name')
#     print(ratings)
#     print()
#     # Apply Filter
#     restaurant_type = Restaurant.TypeChoices.BANGLADESHI
#     ratings = Rating.objects.filter(restaurant__restaurant_type=restaurant_type)
#     print(ratings)


# from django.db.models.functions import Lower


# def run():
#     restaurants = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.BANGLADESHI).values_list(Lower('name'), 'date_opened').first()
#     print(restaurants[0], restaurants[1])
    
#     # flat function
    
#     sales = Sale.objects.values_list('income', flat=True)
    
#     print(sales)
    
#     for sale in sales:
#         print(sale)



# Aggregation

from django.db.models import Count, Avg, Max, Min, StdDev, Sum

def run():
    # we can count no of row in restaurant table with count function 
    print(Restaurant.objects.count())
    
    
    # we can use filter function with count 
    # print(connection.queries)
    
    print(Restaurant.objects.filter(name__startswith='c').count())
    
    # Django has additional Method for aggregation that is aggregate. In this method more complex aggregation can be perform. For this example we need to import Count function of django.db.models
    
    
    # we can count individual row with this count function
    
    print(Restaurant.objects.aggregate(Count('id')))
    

    
    # pprint(connection.queries)
    
    """ 
    'sql': 'SELECT COUNT("core_restaurant"."id") AS "id__count" FROM '
    '"core_restaurant"',
    'time': '0.000'
    """
    
    # Here we see alias is id_count which is default. we can change it as our wish
    
    print(Restaurant.objects.aggregate(total=Count('id')))
    
    # Aggregate function is a terminal function for Django Queryset. It return a dictionary we can not chain additional function on to that. So Return key value pairs representing the aggregations that your're performing. You can then filter function after that's because this is a terminal clause for a query set 
    
    # Average
    print(Rating.objects.aggregate(avg=Avg('rating')))
    
    # Apply Filter Function
    print(Rating.objects.filter(restaurant__name__startswith='c').aggregate(avg=Avg('rating')))
    
    # Min, Max Function
    print(Sale.objects.aggregate(max=Max('income')))
    print(Sale.objects.aggregate(min=Min('income')))
    
    # Can  Aggregate function take multiple argument
    print(Sale.objects.aggregate(
        max=Max('income'),
        min=Min('income'),
        avg=Avg('income'),
        staDv=StdDev('income'),
        total=Sum('income')
    ))

    # Aggregate subset of value
    one_month_ago = timezone.now() - timezone.timedelta(days=31)
    
    sales = Sale.objects.filter(datetime__gt=one_month_ago).aggregate(total=Sum('income'))
    print(sales)
