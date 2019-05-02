from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "service"

urlpatterns = [

    url(r'^update_verify/$',views.update_verify, name="update_verify"),
    url(r'^check_update_status/$',views.get_update_status, name="check_update_status"),
    #url(r'^complaint/$',views.complaint, name="complaint"),
    url(r'^complaint_front/$',views.complaint_front, name="complaint_front"),
    #url(r'^check_enroll_id/$', views.check_enroll_id, name='check_enroll_id'),
    #url(r'^autofill1_check/$', views.autofill1_check, name='autofill1_check'),
    url(r'^complaint/$', views.complaint, name='autofill1'),
    url(r'^check_enroll_id/$', views.check_enroll_id, name='check_enroll_id'), # check weather enroll_id in complaint form exsists or not
    url(r'^autofill1_check/$', views.autofill1_check, name='autofill1_check'),
    url(r'^complaint_status/$', views.complaint_status, name='complaint_status'),

    url(r'^verify_aadhar/$', views.verify_aadhar, name='verify_aadhar'), # verify aadhar eists or not
    url(r'^verify_mobile_email/$', views.verify_mobile_mail, name='verify_mobile_mail'),
    url(r'^verify_otp/$', views.verify_otp, name='verify_otp'),

    url(r'^offline_ekyc/$', views.offline_ekyc, name='offline_ekyc'),
    url(r'^offline_ekyc_otp/$', views.offline_ekyc_otp, name='offline_ekyc_otp'),

    url(r'^address_status/$', views.address_status, name='address_status'),
    url(r'^address_status_result/$', views.address_status_result, name='address_status_result'),

    url(r'^bank_linking/$', views.bank_linking, name='bank_linking'),
    url(r'^bank_linking_otp/$', views.bank_linking_otp, name='bank_linking_otp'),
    #url(r'^complaint_status/$', views.complaint_status_resu, name='complaint_status_result'),


]
