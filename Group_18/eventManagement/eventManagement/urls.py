"""eventManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from fundraiser import views as pay
from userActivity import views as activity

urlpatterns = [
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="home/reset_password_complete.html"), name="password_reset_complete"),
    path('admin/', admin.site.urls),
    #path('home/', include('home.urls')),
    path('home/', include('home.urls')),
    path('events/', include('events.urls')),
    path('groups/',include('groups.urls')),
    path('shop/', include('shop.urls')),
    path('chat/', include('chat.urls')),
    path('fundraiser/', include('fundraiser.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-button/', pay.payment_button, name='payment-button'),
    path('payment-done/', pay.payment_done, name='payment_done'),
    path('payment-cancelled/', pay.payment_cancelled, name='payment_cancelled'),
    path('user-activity/',include('userActivity.urls'))
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# activity.userActivity(repeat=604800,repeat_until=None)
