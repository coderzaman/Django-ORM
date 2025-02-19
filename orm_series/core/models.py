from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Restaurant 
# User
# Rating
class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name

