from django.urls import path
from rentedcars import views
from django.conf import settings
from django.conf.urls.static import static


app_name='rentedcars'


urlpatterns = [
    path('rentcardisplay/',views.rentcardisplay,name='rentcardisplay'),
    path('display_avail_cars/',views.display_avail_cars,name='display_avail_cars'),
    path('rentcarform/',views.rentcarform,name='rentcarform'),
    # path('bookcabform/',views.bookcabform,name='bookcabform'),
    path('book/(<int:book_id>)',views.book_my_car,name='book_my_car'),
    path('display_req/',views.display_req,name='display_req'),
    path('display_req/(<int:req_id>)',views.accept,name='display_req_accept'),
    path('history/',views.rentalhistory,name='rentalhistory'),
    path('cab_trip/',views.cab_trip,name='cab_trip'),
    path('endcabtrip/(<int:endcab_id>)',views.endcabtrip,name='endcabtrip'),
    path('trial/<int:trial_id>)',views.trial,name='trial'),
    path('car_history/',views.car_view_history,name='car_history'),
    path('display_map/(<int:map_id>)',views.display_map,name='display_map')
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
