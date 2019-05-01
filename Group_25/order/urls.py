from django.urls import path
from order import views
app_name = 'order'

urlpatterns = [
    path('<int:item_id>/', views.add_to_cart, name='pick'),
    path('remove/<int:cart_item_id>/', views.remove_cart_item, name='remove'),
    path('cart/', views.check_cart_items, name='cart'),
    path('order/', views.order, name='order'),
    path('order_items/', views.order_items, name='order_items'),
    path('order_history/', views.order_history, name='history'),
    path('history_items/<int:order_id>/', views.order_history_items, name='history_items'),
    path('check/<int:order_id>/', views.check_order_payment, name='payment_details')
]