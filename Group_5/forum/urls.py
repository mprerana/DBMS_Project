from django.urls import path, include
from . import views
app_name='forum'

urlpatterns = [
    path('', views.forum,name="forum"),
]
