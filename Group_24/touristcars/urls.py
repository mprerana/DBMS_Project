from django.urls import path
from touristcars import views
from django.conf import settings
from django.conf.urls.static import static


app_name='touristcars'

urlpatterns = [
    path('booktour/',views.booktour,name='booktour'),
    path('booktourcar/(<int:tour_id>)',views.booktourcar,name='booktourcar'),
    path('touristcars_history/',views.tourists_view_history,name='touristcars_history'),
    path('display_map/(<int:map_id>)',views.display_map,name='display_map')
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
