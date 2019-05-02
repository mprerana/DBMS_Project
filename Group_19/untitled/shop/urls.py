from django.urls import path, include
from django.conf.urls import url
from shop import views

app_name = 'shop'

urlpatterns = [

    path('create_shop/',views.makeshop,name='create_shop'),
    url(r'listshops/viewshop/(?P<sid>\w+)/$',views.viewshop,name='viewshop'),
    path('listshops/',views.listshops,name='listshops'),
    path('categlistshops/<int:category>/',views.categlistshops,name='categlistshops'),
    path('writereview/<int:sid>/',views.reviewtext,name='writereview'),
    url(r'category/',views.category,name='category')

]