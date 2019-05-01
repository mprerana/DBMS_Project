from django.urls import path, include
from adverisements import views

app_name = 'advertisements'

urlpatterns = [

    path('create_adv/',views.makeadv,name='create_adv'),
    path('viewadv/<int:adv_id>/',views.viewadv,name='viewadv'),
    path('listadv/',views.listadv,name='listadv')


]