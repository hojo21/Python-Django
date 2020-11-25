from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("<int:id>", views.index, name="index"),
    # path("<str:name>", views.index, name="index"),
]