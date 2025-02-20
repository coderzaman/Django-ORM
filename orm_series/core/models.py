from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Restaurant 
# User
# Rating
class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        BANGLADESHI = "BD", "Bangladeshi"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        FASTFOOD = "FF", "Fast Food"
        OTHER = "OT", "Other"
        DEFAULT = "", "-------Select Option-------"
    
    name = models.CharField(max_length=150)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, default=TypeChoices.DEFAULT, choices=TypeChoices.choices)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    
    class Rating(models.TextChoices):
        WORST = "1", "Worst"
        BAD = "2", "Bad"
        NOTBAD = "3", "Not Bad"
        GOOD = "4", "Good"
        EXCELLENT = "5", "Excellent" 
        DEFAULT = "", "----Select Your Option---" 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.CharField(default=Rating.DEFAULT, choices=Rating.choices, max_length=1)
    
    def __str__(self):
        return f'Rating: {self.rating}'

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2) #This are the required?
    datetime = models.DateTimeField()