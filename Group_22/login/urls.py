from django.urls import path,include, re_path
from . import views

app_name = 'login'

urlpatterns = [
    re_path('^$', views.home, name="login.home"),
    path('accounts/', views.user_login, name="login.user_login"),
    path('logout/',views.logoutuser, name="logout")

]
