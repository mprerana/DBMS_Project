from django.conf.urls import url
from django.urls import path
from . import views

app_name='funds'

urlpatterns=[
    path('home_with_pk/(?P<pk>\d+)/', views.home, name='home_with_pk'),
]
