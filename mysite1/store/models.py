from django.db import models

# Create your models here.

# this is the data type for the customers. it can store a CharField for the customer's name and information
class ShoppingCart(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# this is the data type for the items that the customers buy. it can store a CharField for the item names and can be changed
class Item(models.Model):
    shoppingcart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text