from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation



# Custom Validator 
def start_with_a(value):
    if not value.startswith("a"):
        raise ValidationError("Restaurant name Start with a")


from django.db.models.functions import Lower


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        BANGLADESHI = "BD", "Bangladeshi"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        MEXICAN = "MX", "Mexican"
        FASTFOOD = "FF", "Fast Food"
        OTHER = "OT", "Other"
        DEFAULT = "", "-------Select Option-------"
    
    name = models.CharField(max_length=150, validators=[start_with_a])
    restaurant_type = models.CharField(max_length=2, default=TypeChoices.DEFAULT, choices=TypeChoices.choices)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    capacity = models.SmallIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)
    comments = GenericRelation('Comment', related_query_name='restaurant')    
    
    # class Meta:
    #     ordering = ['name', 'date_opened']
    #     get_latest_by = 'date_opened'  # Sets default field for latest()
    def save(self, *args, **kwargs):
        
        print(self._state.adding) # False = UPDATE, True = INSERT
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
class Staff(models.Model):
    name = models.CharField(max_length=12)
    restaurants = models.ManyToManyField(Restaurant, through="StaffRestaurant")
    
    def __str__(self):
        return self.name

class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)

class Rating(models.Model):
    
    # class Rating(models.TextChoices):
    #     WORST = "1", "Worst"
    #     BAD = "2", "Bad"
    #     NOTBAD = "3", "Not Bad"
    #     GOOD = "4", "Good"
    #     EXCELLENT = "5", "Excellent" 
    #     DEFAULT = "", "----Select Your Option---" 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='ratings')
    # rating = models.CharField(default=Rating.DEFAULT, choices=Rating.choices, max_length=1)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comments = GenericRelation('Comment')
    
    def __str__(self):
        return f'Rating: {self.rating}'

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2) #This are the required
    expenditure = models.DecimalField(max_digits=8, decimal_places=2) #This are the required
    datetime = models.DateTimeField()
    
    def __str__(self):
        return f'{self.restaurant.name}, Income: {self.income}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    number_in_stock = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f'{self.number_of_items} X {self.product.name}'

# Crate a model named which will accessible to all other models
class Comment(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    

