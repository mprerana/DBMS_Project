from django.conf.urls import url
from django.urls import path
from . import views
from userlogin import views as prof

app_name='admin_login'

urlpatterns=[
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('req_appoint/(?P<pk>\d+)/', views.req_appoint, name='req_appoint'),
    path('req_cancel/(?P<pk>\d+)/', views.req_cancel, name='req_cancel'),
    path('req2_verify/(?P<pk>\d+)/', views.req2_verify, name='req2_verify'),
    path('req2_cancel/(?P<pk>\d+)/', views.req2_cancel, name='req2_cancel'),
    #path('eventsverify/', views.verifyevents, name='verifyevents'),
    path('verifyevent/', views.verifyevent, name='verifyevent'),
    path('prof/', prof.edit_profile, name="profile")
]
