from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Custom Validator 
def start_with_a(value):
    if not value.startswith("a"):
        raise ValidationError("Restaurant name Start with a")


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        BANGLADESHI = "BD", "Bangladeshi"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        FASTFOOD = "FF", "Fast Food"
        OTHER = "OT", "Other"
        DEFAULT = "", "-------Select Option-------"
    
    name = models.CharField(max_length=150, validators=[start_with_a])
    restaurant_type = models.CharField(max_length=2, default=TypeChoices.DEFAULT, choices=TypeChoices.choices)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    
    def save(self, *args, **kwargs):
        
        print(self._state.adding)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

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
    
    def __str__(self):
        return f'Rating: {self.rating}'

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2) #This are the required
    datetime = models.DateTimeField()