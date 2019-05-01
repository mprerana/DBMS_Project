from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from . import views
from service import views as service_view
from history import views as history_view



urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^home/$',views.home, name="base"),
    path('update/',include("update.urls")),
    path('aadharcard/',include("aadharcard.urls")),
    url(r'^captcha/', include('captcha.urls')),   # Captcha
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), # CK editor
    url(r'^datetimepicker/', include('datetimepicker.urls')),
    path('service/', include('service.urls')),
    url(r'^test/$',views.test, name="test"),
    path('',views.uidai_home, name= "uidai_home"),


    url(r'^login/$',views.login_view, name="login"),
    url(r'^logout/$',views.logout_view, name="logout"),
# na
    path('nearest_centre/',views.nearest_centre,name = 'nearest_centre'),
# sk
    path('history/ServiceRegister', history_view.ServiceRegister, name='service'),
    path('history/validation', history_view.validation, name='validation'),
    path('history/get_history', history_view.get_history, name='history'),

    url(r'^complaint_check/$', views.complaint_check, name='complaint_check'), # Check all complaints (Authentication required)
    url(r'^complaint_reply/(?P<id>\d+)/$', views.complaint_reply, name='complaint_reply'), # Replay to each complaint

    url(r'^address_update_check/$', views.address_update_check, name='address_update_check'),
    url(r'^address_update_check_reply/(?P<id>\d+)/$', views.address_update_check_reply, name='address_update_check_reply'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
