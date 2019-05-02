
from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.conf.urls import include

app_name = 'songs'

urlpatterns = [
    #re_path('^$', views.index,name = 'force.index'),
    #path('result/',views.result,name="force.result")
    #path('',views.home, name='home'),
]
