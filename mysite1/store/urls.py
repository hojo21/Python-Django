from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("cart/", views.cart, name="cart"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home")
    # path("<str:name>", views.index, name="index"),
]