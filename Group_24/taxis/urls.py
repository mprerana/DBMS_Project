from django.urls import path
from taxis import views

app_name='taxis'

urlpatterns = [
    path('booktaxi/',views.booktaxi,name='booktaxi'),
    path('avail_taxi/',views.avail_taxi,name='avail_taxi'),
    path('accept_taxi/(<int:accept_id>)',views.accept_taxi,name='accept_taxi'),
    path('your_trip/',views.your_trip,name='your_trip'),
    path('endtrip/(<int:end_id>)',views.endtrip,name='endtrip'),
    # path('all_trips/',views.all_trips,name='all_trips'),
    path('book_driver/',views.book_driver,name='book_driver'),
    path('book_d/(<int:driver_id>)',views.book_d,name='book_d'),
    path('display_map/(<int:map_id>)',views.display_map,name='display_map'),
    path('taxi_view_history/',views.taxi_view_history,name='taxi_view_history'),

]
