from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('', views.review_list, name='review_list'),
    path('fill',views.add_review, name='add_review' ),
    #path('filtered',views.filterreview, name='filterreview')
    ]