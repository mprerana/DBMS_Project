from django.conf.urls import include, url
from paytm import views as paytm_views

app_name="paytm"

urlpatterns = [
    # Examples:
    url(r'^$', paytm_views.home, name='paytm.home'),
    url(r'^payment/', paytm_views.payment, name='payment'),
    url(r'^response/', paytm_views.response, name='response'),
]
