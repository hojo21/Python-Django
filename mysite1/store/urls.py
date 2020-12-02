from django.urls import path

from . import views

# these are the different paths for the url in order to navigate to the different pages
urlpatterns = [
    # path("", views.index, name="index"),
    
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("<int:id>", views.index, name="index"),
    # path("<str:name>", views.index, name="index"),
]