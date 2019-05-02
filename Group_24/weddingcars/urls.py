from django.urls import path
from weddingcars import views
from django.conf import settings
from django.conf.urls.static import static


app_name='weddingcars'

urlpatterns = [
    path('weddingcardisplay/',views.weddingcardisplay,name='weddingcardisplay'),
    path('weddingcar_book/(<int:wed_id>)',views.weddingcar_book,name='weddingcar_book'),
    path('weddingcars_history/',views.tourists_view_history,name='weddingcars_history'),
    path('display_map/(<int:map_id>)',views.display_map,name='display_map')
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
