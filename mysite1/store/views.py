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

    #{"save":["save"], "c1":["clicked"]}
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else: 
                    item.complete = False

                item.save()
                
        elif response.POST.get("newItem"):
            txt= response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

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