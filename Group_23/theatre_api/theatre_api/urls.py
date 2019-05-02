from django.contrib import admin
from django.urls import path
from movie_and_cinema_data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movie', views.movie_data.as_view()),
    path('api/theatre', views.theatre_data.as_view()),
    path('api/screen',views.screen_data.as_view()),
    path('api/ticket',views.ticket_data.as_view()),
    path('api/bookedticket',views.booked_ticket_data.as_view()),
    path('api/movie_changes',views.movie_update_data.as_view()),
    path('api/theatre_changes', views.theatre_update_data.as_view()),
    path('api/screen_changes',views.screen_update_data.as_view()),
    path('api/ticket_changes',views.ticket_update_data.as_view()),
]
