from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'shop'

urlpatterns = [
    # /myApp/
    path('', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.add_to_cart, name='add_to_cart'),
    #url(r'medicine/add/$', views.CartView.as_view(), name='cart-add'),
    url(r'^finalPrice/(?P<order_id>[0-9]+)/$', views.finalPrice, name='finalPrice'),
    url(r'^checkout/(?P<order_id>[0-9]+)/$', views.checkout, name='checkout'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('order-summary/', views.order_details , name="order_summary"),
    path('checked-products/', views.checked , name="checked"),
    #path('order-summary/', views.order_details , name="order_summary"),
    url(r'^item/delete/(?P<item_id>[0-9]+)/$', views.delete_from_cart, name='delete_item'),
    url(r'^order/delete/(?P<order_id>[0-9]+)/$', views.delete_order, name='delete_order'),
    path('send/', views.send, name='send'),
]
