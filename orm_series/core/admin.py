from django.contrib import admin
from core.models import Restaurant, Sale, Rating, Product, Order, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
class CommentInline(GenericTabularInline):
    model = Comment
    max_num = 1

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [CommentInline]


admin.site.register(Restaurant, RestaurantAdmin)
    
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'content_type', 'object_id', 'content_object']




admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Order)

