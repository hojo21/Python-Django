from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShoppingCart, Item
from .forms import CreateNewCart

# Create your views here.

# def index(response, id): 
#     return HttpResponse("<h1>store front page</h1><h1>%s</h1>" % id)

# Dynamic store pages based off of query id number example
# def index(response, id): 
#     ls = ShoppingCart.objects.get(id=id)
#     return HttpResponse("<h1>Dynmaic store page for: %s</h1>" %ls.id)

# Rendering the html pages for the store
def index(response, id):  
    ls = ShoppingCart.objects.get(id=id)
    return render(response, "store/cart.html", {"ls":ls})

def home(response): 
    return render(response, "store/home.html", {})

def cart(response): 
    return render(response, "store/cart.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewCart(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ShoppingCart(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewCart()

    return render(response, "store/create.html", {"form":form})