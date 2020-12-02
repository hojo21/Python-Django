from django.contrib import admin
from .models import ShoppingCart, Item

# Register your models here.
# This is where the models created on models.py are registered and connected to the admin page 

admin.site.register(ShoppingCart)
admin.site.register(Item)