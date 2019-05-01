from django.urls import path

from . import views
from Paypal import views
from . import views


app_name='funding'

urlpatterns = [
    path('', views.index, name='index'),
    path('startproject', views.startproject, name='startproject'),
    path('donate',views.donate, name='donate'),
]
