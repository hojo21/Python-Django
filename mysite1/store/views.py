from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response): 
    return HttpResponse("<h1>store front page</h1>")

def cart(response):
    return HttpResponse("<h1>Shopping Cart</h1>")