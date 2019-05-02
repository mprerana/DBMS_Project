from django.urls import path
from airportcars import views
from django.conf import settings
from django.conf.urls.static import static


app_name='airportcars'

urlpatterns = [
    path('bookairportcar/',views.bookairportcar,name='bookairportcar'),
    path('book_a_car/(<int:air_id>)',views.book_a_car,name='book_a_car'),
    path('airportcars_history/',views.tourists_view_history,name='airportcars_history'),
    path('display_map/(<int:map_id>)',views.display_map,name='display_map')

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
