
from django.contrib import admin
from django.urls import path
from core import views


from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.home, name='home'),
] + debug_toolbar_urls()
