from django.contrib import admin
from django.urls import path,include
from accounts import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('accounts/',include('accounts.urls')),
    path('rentedcars/',include('rentedcars.urls')),
    path('taxis/',include('taxis.urls')),
    path('contacts/',include('emergencycontacts.urls')),
    path('tourist/',include('touristcars.urls')),
    path('weddingcar/',include('weddingcars.urls')),
    path('airportcars/',include('airportcars.urls')),
    path('notifications/',include('notifications.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
