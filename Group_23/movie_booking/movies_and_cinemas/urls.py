from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path,include
import registration
from payment import views as view1
appname = "movies_and_cinemas"

urlpatterns = [
path('<str:city>/payment1/',views.payment,name='payment'),
path('/<str:city>/',include('registration.urls')),
path('',views.city,name='city'),

path('1/payment/', view1.pay, name='pay'),
path('1/payment/check', view1.check, name='check'),
path('1/payment/status/', view1.status, name='status'),
path('1/payment/fineform/', view1.pay_fine, name='payfine'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)