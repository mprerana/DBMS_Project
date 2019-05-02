"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from homepage import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('django.contrib.auth.urls')),
    path('br/',include('plot.urls')),
    path('paypal/', include('credits.urls')),
    path('', views.index, name='index'),
    path('homepage/', include('homepage.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    path('feedback/', views.display_feedback, name='display_feedback'),
    path('shop/', include('shop.urls')),
    path('advertisements/', include('adverisements.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
