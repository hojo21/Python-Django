from django.contrib import admin
from .models import ShoppingCart, Item

# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(Item)