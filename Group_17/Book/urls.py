from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   #path('flight/', views.flight_book, name='flight'),
   path('flight_search/',views.flight_search, name='flight_search'),
   path('hotel_book/',views.hotel_book,name='hotel_book'),
   path('booked/',views.booked , name='booked'),
   path('ticket_book/',views.ticket_book , name='ticket_book'),
   path('hotel_search/',views.hotel_search,name='hotel_search'),
   path('hotel_details/',views.hotel_details,name='hotel_details'),
   path('flights_booked/',views.flight_view,name='flights_booked'),
   path('hotels_booked/', views.hotel_view, name='hotels_booked'),

   #path('show/',views.showed,name='showed'),
   #path('show1/',views.hotel_showed,name='hotel_showed'),

]