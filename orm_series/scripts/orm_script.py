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

# from django.db.models import Count, Avg, Max, Min, StdDev, Sum

# def run():
#     # we can count no of row in restaurant table with count function 
#     print(Restaurant.objects.count())
    
    
#     # we can use filter function with count 
#     # print(connection.queries)
    
#     print(Restaurant.objects.filter(name__startswith='c').count())
    
#     # Django has additional Method for aggregation that is aggregate. In this method more complex aggregation can be perform. For this example we need to import Count function of django.db.models
    
    
#     # we can count individual row with this count function
    
#     print(Restaurant.objects.aggregate(Count('id')))
    

    
#     # pprint(connection.queries)
    
#     """ 
#     'sql': 'SELECT COUNT("core_restaurant"."id") AS "id__count" FROM '
#     '"core_restaurant"',
#     'time': '0.000'
#     """
    
#     # Here we see alias is id_count which is default. we can change it as our wish
    
#     print(Restaurant.objects.aggregate(total=Count('id')))
    
#     # Aggregate function is a terminal function for Django Queryset. It return a dictionary we can not chain additional function on to that. So Return key value pairs representing the aggregations that your're performing. You can then filter function after that's because this is a terminal clause for a query set 
    
#     # Average
#     print(Rating.objects.aggregate(avg=Avg('rating')))
    
#     # Apply Filter Function
#     print(Rating.objects.filter(restaurant__name__startswith='c').aggregate(avg=Avg('rating')))
    
#     # Min, Max Function
#     print(Sale.objects.aggregate(max=Max('income')))
#     print(Sale.objects.aggregate(min=Min('income')))
    
#     # Can  Aggregate function take multiple argument
#     print(Sale.objects.aggregate(
#         max=Max('income'),
#         min=Min('income'),
#         avg=Avg('income'),
#         staDv=StdDev('income'),
#         total=Sum('income')
#     ))

#     # Aggregate subset of value
#     one_month_ago = timezone.now() - timezone.timedelta(days=31)
    
#     sales = Sale.objects.filter(datetime__gt=one_month_ago).aggregate(total=Sum('income'))
#     print(sales)

# # Annotation
# # Difference between aggregation and annotation is that when you annotate values you're going to get a value added to each model in the queryset. That you have coming back from annotate function whereas the aggregate function does not do that. It returns a single value based on the aggregation so when you use the annotate function, that we're about to see rather then breaking all of the rows down to a single value the annotation is going to be applied to all of the model on the queryset. So Annotation can add new and important data to your Django models in a queryset.
# from django.db.models import Count, Sum, CharField, Value, Avg
# from django.db.models.functions import Upper, Length, Concat

# def run():
#     # Fetch all restaurants and get length of restaurant of each restaurant name
#     restaurants = Restaurant.objects.annotate(res_len=Length('name'))
    
#     print(restaurants) # It return which have an extra field name res_len with existing field
    
#     # If we see this len of first restaurant
#     print(restaurants.first().res_len)
    
#     # To get all restaurant and values 
#     print(restaurants.values('name', 'res_len'))
    
#     print()
#     # we can use filter statements with it
#     print(Restaurant.objects.annotate(res_len = Length('name')).filter(res_len__gt=10).values('name', 'res_len'))

#     # Concat: Another database function coming from database function module that is Concat that's used to concatenate two or more fields from the database
    
#     # Restaurant 1 [Rating: 4.3]
#     # Value() = Value function add string with database field
#     concatenation = Concat(
#         'name', Value(' [Rating: '), Avg('ratings__rating'), Value(']'),
#         output_field=CharField() # Giving the concatenation as string
#     )
    
#     restaurants = Restaurant.objects.annotate(message=concatenation)
    
#     for r in restaurants:
#         print(r.message)
        
#     print()
    
#     # Total Sales of each restaurants 
#     res_sales = Restaurant.objects.annotate(total_sale=Sum('sales__income')).values('name','total_sale')
   
#     # res_sales = res_sales.
    
#     for r in res_sales:
#         print(r['name'], r['total_sale'])
        
#     # Get count rating of each restaurant
#     print()
#     print()
#     res_ratings = Restaurant.objects.annotate(count_rate=Count('ratings'))
    
#     for r in res_ratings:
#         print(r.name, r.count_rate)
    
#     print()
#     print()
#     # Sum of rating per restaurants
#     res_ratings = Restaurant.objects.annotate(total_rate=Sum('ratings__rating'))
    
 
#     for r in res_ratings:
#         print(r.name, r.total_rate)
    
    
#     # Get average rating for each restaurant 
#     res_ratings = Restaurant.objects.annotate(avg_rate=Avg('ratings__rating'))
    
#     for r in res_ratings:
#         print(r.avg_rate)
    
#     # Ordinarily, annotations are generated on a per-object basis - an annotated QuerySet will return one result for each object in the original QuerySet. However, when a values() clause is used to constrain the columns that are returned in the result set, the method for evaluating annotations is slightly different. Instead of returning an annotated result for each result in the original QuerySet, the original results are grouped according to the unique combinations of the fields specified in the values() clause. An annotation is then provided for each unique group; the annotation is computed over all members of the group.
    
#     print()
#     print()
    
#     rating_count_base_type = Restaurant.objects.values('restaurant_type').annotate(rate_count=Count('ratings'))  
    
#     print(rating_count_base_type)
    
        
#     print()
#     print()
    
    
#     # ordered by function
#     total_sale = Restaurant.objects.annotate(total_sale=Sum('sales__income')).order_by('total_sale')
    
#     # for descending order we can extra - before total_sale
#     #  total_sale = Restaurant.objects.annotate(total_sale=Sum('sales__income')).order_by('-total_sale')
    
#     for sale in total_sale:
#         print(sale.name, sale.total_sale)
    
          
#     print()
#     print()
    
    
#     # filter  function
#     total_sale = Restaurant.objects.annotate(total_sale=Sum('sales__income')).order_by('total_sale').filter(total_sale__lte=300)
    
#     for sale in total_sale:
#         print(sale.name, sale.total_sale)
    
#     # Apply aggregation on annotation field
#     avg_sale = total_sale.aggregate(Avg('total_sale'))
#     print(avg_sale)


# def run():
#     rating = Rating.objects.filter(rating__lte=3).first()
    
#     # Rating here pull database into python memory execute calculation and then push it again to database 
#     rating.rating +=  1
#     rating.save()
#     pprint(connection.queries)
#     """
#         [{'sql': 'SELECT "core_rating"."id", "core_rating"."user_id", '
#          '"core_rating"."restaurant_id", "core_rating"."rating" FROM '
#          '"core_rating" WHERE "core_rating"."rating" <= 3 ORDER BY '
#          '"core_rating"."id" ASC LIMIT 1',
#         'time': '0.000'},
#         {'sql': 'UPDATE "core_rating" SET "user_id" = 1, "restaurant_id" = 3, '
#                 '"rating" = 2 WHERE "core_rating"."id" = 1',
#         'time': '0.003'}]
#     """

# Django Q Objects

# Complex lookups with Q objects¶
# Keyword argument queries – in filter(), etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.

# A Q object (django.db.models.Q) is an object used to encapsulate a collection of keyword arguments. These keyword arguments are specified as in “Field lookups"

# from django.db.models import Q, F 

# def run():
#     # Get all Italian or Mexican Restaurant
#     it = Restaurant.TypeChoices.ITALIAN
#     mex = Restaurant.TypeChoices.MEXICAN
    
#     # restaurants = Restaurant.objects.filter(restaurant_type=it, restaurant_type=mex)  # SyntaxError: keyword argument repeated: restaurant_type
    
#     # Solve this problem with Q Objects
#     restaurants = Restaurant.objects.filter(
#         Q(restaurant_type=it) | Q(restaurant_type=mex)
#     ).values('name')

    
#     for r in restaurants:
#         print(r['name'])
    
#     pprint(connection.queries)
    
    
#     # Filtering with OR and NOT Conditions
#     # Select those restaurants which name contains mexican or italian
#     # restaurants = Restaurant.objects.filter(
#     #  name__icontains=['italian','mexican']
#     # ).values('name')
    
#     # Not work cause icontains or any other most of the function take string not list. For solve this problem we need to solve with Q Objects
    
#     restaurants = Restaurant.objects.filter(
#      Q(name__icontains='italian') | Q(name__icontains='mexican')
#     ).values('name')
#     for r in restaurants:
#         print(r['name'])
#     # Select those restaurants which name contains mexican or italian or recently opened
    
#     it_or_max = Q(name__icontains='italian') | Q(name__icontains='mexican')
  
    
#     recently_opened = Q(date_opened__gt = timezone.now() - timezone.timedelta(days=40))
#     restaurants = Restaurant.objects.filter(it_or_max  | recently_opened)
    
#     print(restaurants)
    
#     # for recently not opened 
#     recently_not_opened = ~ Q(date_opened__gt = timezone.now() - timezone.timedelta(days=40))
#     restaurants = Restaurant.objects.filter(it_or_max  | recently_not_opened)
    
#     print(restaurants)
    
#     # More Complex Example:
#     # - profit is greater then expenditure, OR
#     # - restaurant name contains a number
    
#     name_has_num = Q(restaurant__name__regex=r"[0-9]+")
#     profited = Q(income__gt=F('expenditure'))
    
#     print()
 
#     sales = Sale.objects.filter(name_has_num | profited).values_list('restaurant__name',flat=True)
#     # we can use also and here 
#     # - profit is greater then expenditure, and
#     # - restaurant name contains a number
#     print()
#     sales = Sale.objects.filter(name_has_num & profited).values_list('restaurant__name',flat=True)
#     print(sales)
#     print()
#     # we optimize query using select_related or prefetch related
#     sales = Sale.objects.filter(name_has_num & profited).select_related('restaurant').values_list('restaurant__name',flat=True)
    
#     for sale in sales:
#         print(sale)


# Django - COALESCE Function and Handling NULL Values in the Database

# Adding a nullable field to a Django Model
# add new field to restaurant, which default value is null
# capacity = models.SmallIntegerField(null=True, blank=True)

# Querying null data with “is null” lookup
# from django.db.models import Sum
# from django.db.models.functions import Coalesce
# from django.db.models import F, Count, Q, Avg
# import random
# def run():
#     restaurants = Restaurant.objects.filter(capacity__isnull=True)
#     print(restaurants)
    
#     restaurants = Restaurant.objects.all()[:2]
    
#     for restaurant in restaurants:
#         restaurant.capacity = random.uniform(50,100)
    
#     print()
#     print()
#     Restaurant.objects.bulk_update(restaurants, ['capacity'])
#     restaurants = Restaurant.objects.filter(capacity__isnull=False)
#     print(restaurants)
    
# # Null values and String-Based fields (CharField, etc)
# # If True, Django will store empty values as NULL in the database. Default is False.

# # Avoid using null on string-based fields such as CharField and TextField. If a string-based field has null=True, that means it has two possible values for “no data”: NULL, and the empty string. In most cases, it’s redundant to have two possible values for “no data;” the Django convention is to use the empty string, not NULL. One exception is when a CharField has both unique=True and blank=True set. In this situation, null=True is required to avoid unique constraint violations when saving multiple objects with blank values.

# # In Restaurant model we add website filed as default empty string. Here we use URL field which subclass of url field
# # for example
# # website = models.URLField(default='', blank=True)


# # Ordering with null values in Django with order_by function
# # Default it order null value first and not null value in the last
   
#     print()
#     print(
#         Restaurant.objects.order_by('capacity').values_list('capacity', flat=True)
#     )
# # <QuerySet [None, None, None, None, None, None, None, None, None, None, None, None, 58, 98]>
#     print()
# #    If we  order fill value first and null will be last we used f expression for this
#     print(
#          Restaurant.objects.order_by(F('capacity').asc(nulls_last=True)).values_list('capacity', flat=True)
#     )
    
#     # If do not dill with the null value there is another way to doing thats
#     print(
#          Restaurant.objects.filter(capacity__isnull=False).order_by('capacity').values_list('capacity', flat=True)
#     )
    
#     # COALESCE function in Django and databases
#     # Accepts a list of at least two field names or expressions and returns the first non-null value (note that an empty string is not considered a null value). Each argument must be of a similar type, so mixing text and numbers will result in a database error. 
    
#     Restaurant.objects.update(capacity=None)
    
#     print(
#         Restaurant.objects.aggregate(total_cap=Sum('capacity'))
#     )
    
#     # {'total_cap': None}
    
#     # If we calculation any value always a number we solve this problem with Coalesce
#     # If there is null value after calculation we grantee eliminate null value and given number or anything instead of it
#     print(
#         Restaurant.objects.aggregate(total_cap=Coalesce(Sum('capacity'),0))
#     )
    
#     # when calculate avg in empty query set ot gives None
#     print(
#         Rating.objects.filter(rating__lt=0).aggregate(total_avg=Avg('rating'))
#     )
    
#     # If eliminate it we can use Coalesce function here
#     print(
#         Rating.objects.filter(rating__lt=0).aggregate(total_avg=Coalesce(Avg('rating'),0.0))
#     )
    
#     # we can solve it with default parameter
#     print(
#         Rating.objects.filter(rating__lt=0).aggregate(total=Avg('rating', default=0.0))
#     )
    
#     # we add another field to Restaurant model name nickname
#     # nickname = models.CharField(max_length=200, null=True, blank=True
    
#     # we Coalesce use for if value is not found then value filled with another.
#     # Here nickname not found name_value filled with name
    
#     print()
#     print()
#     print(
#         Restaurant.objects.annotate(name_value = Coalesce(F('nickname'), F('name'))).values('name_value')
#     )
    
#     # If we set 1 restaurant nickname set not null value 
#     restaurant = Restaurant.objects.first()
#     restaurant.nickname = "abcd"
#     restaurant.save()
    
#     #Now it show first restaurant name_value as abcd cause nickname is set
#     print(
#  Restaurant.objects.annotate(name_value = Coalesce(F('nickname'), F('name'))).values('name_value')
#     )

# # Django Conditional Expressions / Case() and When() objects

# # A Case() expression is like the if … elif … else statement in Python. Each condition in the provided When() objects is evaluated in order, until one evaluates to a truthful value. The result expression from the matching When() object is returned.

# from django.db.models import F, Q, When,Case, Count, Avg, Value, Min, Max, CharField, Sum
# import itertools
# def run():
    
#     #Fetch Italian Restaurant
#     italian = Restaurant.TypeChoices.ITALIAN
    
#     restaurants = Restaurant.objects.annotate(
#         is_italian = Case(
#             When(restaurant_type=italian, then=True),
#             default=False
#         )
#     ) 
    
#     print(restaurants.filter(is_italian=True))
#     print()
    
#     # Fetch Popular restaurant. Which have more than 8 sales
#     restaurants = Restaurant.objects.annotate(
#         n_sales=Count('sales'),
#         popular_res = Case(
#             When(n_sales__gt=8, then= True),
#             default=False
#         )
#     ).values('name','n_sales','popular_res').order_by('-n_sales')
    
#     print(restaurants.filter(popular_res=True))
#     print()
    
#     # Restaurant average rating > 3.5 and Restaurant has more than 1 rating, Multiple condition on When Clause. It works like and
#     restaurants = Restaurant.objects.annotate(
#         avg_rating=Avg('ratings__rating'),
#         num_rating = Count('ratings__pk'),
#         highly_rated = Case(
#             When(avg_rating__gt=3.5, num_rating__gt=1, then=True),
#             default= False
#         )
        
#     ).values('name', 'avg_rating', 'num_rating').order_by('-avg_rating','-num_rating')
    
#     restaurants = restaurants.filter(highly_rated=True)
    
#     for r in restaurants:
#         print('Restaurant Name:',r['name'],', Ratings:', r['avg_rating'],', No of Ratings:',r['num_rating'])
    
#     print()
    
#     # Multiple when in Case like if elif in python
#     # We can create three bucket for rating 
#     # Highly Rated, Averagely Rated, Badly Rated
    
#     restaurants = Restaurant.objects.annotate(
#         avg_rating=Avg('ratings__rating')
#     )
    
#     restaurants = restaurants.annotate(
#         rating_bucket = Case(
#             When(avg_rating__gt=3.5, then=Value('high')),
#             When(avg_rating__range=(2.5,3.5), then=Value('average')),
#             When(avg_rating__lt=2.5, then=Value('bad')),
#             default=Value('not_rated')
#         )
#     )
    
#     print(restaurants.filter(rating_bucket='not_rated'))
#     print()
    
#     type = Restaurant.TypeChoices
    
#     # Ad continent with Q object in CASE and WHEN
#     restaurants = Restaurant.objects.annotate(
#         continent = Case(
#             When(Q(restaurant_type=type.GREEK) | Q(restaurant_type=type.ITALIAN), then=Value('europe')),
#             When(Q(restaurant_type=type.BANGLADESHI) | Q(restaurant_type=type.CHINESE), then=Value('asian')),
#             When(restaurant_type=type.MEXICAN, then=Value('north-american')),
#             default=Value('N/A')
#         )
#     )
    
#     print(restaurants.filter(continent='asian').order_by('name')) 
    
#     # More clean code 
#     europe = Q(restaurant_type=type.GREEK) | Q(restaurant_type=type.ITALIAN)
#     asia = Q(restaurant_type=type.BANGLADESHI) | Q(restaurant_type=type.CHINESE)
#     north_america = Q(restaurant_type=type.MEXICAN)
    
#     restaurants = Restaurant.objects.annotate(
#         continent = Case(
#             When(europe, then=Value('europe')),
#             When(asia, then=Value('asian')),
#             When(north_america, then=Value('north_american')),
#             default=Value('N/A')
#         )
#     )
    
#     print(restaurants.filter(continent='asian').order_by('name')) 
    
#     print()
#     print()
#     # Aggregating total sales over each 10 day period, starting from the first sale up until the last
#     first_sale = Sale.objects.aggregate(first_sale_date=Min('datetime'))['first_sale_date']
#     last_sale = Sale.objects.aggregate(last_sale_date=Max('datetime'))['last_sale_date']
    
#     dates = []
#     count = itertools.count()
    
#     # divide into each 10 days
#     while(dt := first_sale + timezone.timedelta(days=10*next(count))) <= last_sale:
#         dates.append(dt)
    
#     [print(date) for date in dates]
    
#     whens = [
#         When(datetime__range=(dt, dt+timezone.timedelta(days=10)), then=Value(dt.date()))
#         for dt in dates
#     ]
#     print()
    
#     print('whens: ', whens )
#     print()
    
#     case = Case(
#         *whens,
#         output_field=CharField()
#     )
    
#     print()
#     print(case)
#     print()
    
#     print(Sale.objects.annotate(
#         date_range=case,   
#     ).values('date_range').annotate(total_sales=Sum('income')))
    
# Django - Subquery, OuterRef and Exists objects for Database SQL Subqueries
# A subquery is a query that appears inside another query statement. Subqueries are also referred to as sub- SELECT s or nested SELECT s.



from django.db.models import Subquery, OuterRef, Exists
from django.db.models import F, Q, When,Case, Count, Avg, Value, Min, Max, CharField, Sum

def run():
    
    # Select all sales where restaurant id is IT, CH 
    # SELECT * FROM core_sale
    # WHERE core_sale.restaurant_id IN (SELECT id FROM core_restaurant WHERE restaurant_type IN ('IT', 'CH') )
    # Result: 62 rows returned in 5ms
    
    restaurants = Restaurant.objects.filter(restaurant_type__in=['IT','CH'])
    sales = Sale.objects.filter(restaurant__in = Subquery(restaurants.values('pk')))

    print(sales.count()) # 62
    
    # Select last sale of each restaurant
    # SELECT id, name, restaurant_type, 
    #     (SELECT income FROM core_sale
    #     WHERE restaurant_id=core_restaurant.id 
    #     ORDER BY datetime DESC 
    #     LIMIT 1
    #     ) AS last_sale
    # FROM core_restaurant
    # Result: 14 rows returned in 2ms
    
    
 
    
    # annotate each Restaurant with the income generated from its MOST RECENT sale
    sales = Sale.objects.filter(restaurant=OuterRef('pk')).order_by('-datetime')
    
    # Outer Query 
    restaurants = Restaurant.objects.annotate(
        last_sale_income=Subquery(sales.values('income')[:1])
    )
    
    for r in restaurants:
         print(f"{r.name}: {r.last_sale_income}")

    # We use F expression Here for calculate profit of recent sale
    restaurants = Restaurant.objects.annotate(
        last_sale_income=Subquery(sales.values('income')[:1]),
        last_sale_expenditure=Subquery(sales.values('expenditure')[:1]),
        profit=F('last_sale_income') - F('last_sale_expenditure'),
    )
    
    for r in restaurants:
         print(f"{r.name}: {r.profit}")
    
    
    # Exists objects
    # Exists is a Subquery subclass that uses an SQL EXISTS statement. In many cases it will perform better than a subquery since the database is able to stop evaluation of the subquery when a first matching row is found.

    
    # Filter to restaurants that have any sales with income > 85
    
    restaurants = Restaurant.objects.all()
    print(restaurants.count()) # 14
    
    
    restaurants = Restaurant.objects.filter(
        Exists(Sale.objects.filter(restaurant=OuterRef('pk'), income__gt=85))
    )
    
    print(restaurants.count()) # 6
    
    #we can also not operator here. It is boolean operator.
    restaurants = Restaurant.objects.filter(
        ~Exists(Sale.objects.filter(restaurant=OuterRef('pk'), income__gt=85))
    )
    
    print(restaurants.count()) # 8
    
    # Another Example
    # Find all restaurant have minimum one five starts rating
    restaurants = Restaurant.objects.filter(
        Exists(Rating.objects.filter(restaurant=OuterRef('pk'), rating=5))
    )
    
    print(restaurants)
    
    # All Restaurant that sell of last 30 days
    last_five_days = timezone.now() - timezone.timedelta(days=30) 
    
    restaurants = Restaurant.objects.filter(
        Exists(Sale.objects.filter(restaurant=OuterRef('pk'), datetime__gt=last_five_days))
    )    
    
    print(restaurants)
    
