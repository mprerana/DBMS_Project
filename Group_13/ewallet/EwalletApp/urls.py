from django.urls import path
from EwalletApp import views

app_name = "EwalletApp"
urlpatterns = [
    path("/", views.home, name='home'),
    path("/Signup", views.Register, name='Register'),
    path("/Signin", views.Signin, name='login'),
]
