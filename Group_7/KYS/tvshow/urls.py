from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'tvshow'
urlpatterns = [
    path("tvshow/<int:id>", views.tvshowpage,name='showpage'),
    path("tvshow/<int:series_id>/s<int:season_id>/", views.seasonpage,name='seasonpage'),
    path("tvshow/<int:series_id>/s<int:season_id>/e<int:episodeNum>/", views.episodepage, name='episodepage')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
