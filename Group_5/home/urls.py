from django.urls import path, include
from . import views
app_name='home'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('explore', views.explore, name = 'explore'),
    path('tryout', views.tryout, name = 'tryout'),
    path('recipe/<id>', views.recipe, name='recipe'),
    path('register', views.register, name='register'),
    path('registered', views.registered, name='registered'),
    path('login',views.login, name='login'),
    path('base', views.base, name='base'),
    path('findchefs', views.findchefs, name='find'),
    path('contact', views.contact, name='contact'),
    path('cont', views.cont, name='cont'),
    path('diet', views.diet, name='diet'),
    path('select/<id_1>', views.select, name='select'),
    path('insert', views.insert, name='insert'),
]
