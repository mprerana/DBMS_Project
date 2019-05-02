from django.conf.urls import url
from django.urls import path
from . import views

app_name='customer'

urlpatterns=[
    path('', views.home, name='personal'),
]
