from django import forms
from .models import Restaurant, Rating, Sale, Order

from django.core.validators import MinValueValidator, MaxValueValidator


# we can use validator also in form 
from django import forms
from .models import Restaurant

class ProductStockException(Exception):
    pass

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")  # Only including the relevant fields


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("__all__")
        
    # def save(self, commit = True):
    #     """Check to see if the product has enough items in stock"""
    #     order = super().save(commit=False)
        
    #     if order.product.number_in_stock < order.number_of_items:
    #         raise ProductStockException(
    #             f"Not Enough Item in stock for product: {order.product}"
    #         )
            
    #     if commit: 
    #         order.save()
        
    #     return order