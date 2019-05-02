from django.urls import path,include, re_path
from . import views

app_name="foodtruck"
urlpatterns = [

    path('', views.foodrequest, name='foodtruck.foodrequest'),
]
