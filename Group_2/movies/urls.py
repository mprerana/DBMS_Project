#from django.urls import path,re_path
from . import views
from django.conf.urls import include,url

app_name = 'movies'

urlpatterns = [
    #re_path('^$', views.index,name = 'force.index'),
    #path('result/',views.result,name="force.result")
    url('',views.home, name='home'),
]
