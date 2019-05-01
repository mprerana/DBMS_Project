from django.urls import path
from admin_app import views
app_name = 'admin_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('product/', views.product_report, name='product_report'),
    path('update/<int:item_id>', views.update_product, name='update_product'),
    path('orders/', views.order_report, name='order_report'),
    path('update1/<int:order_id>', views.update_order, name='update_order'),
    path('check/<int:order_id>', views.check_order_items, name='check_order_items'),
    path('check_payment/<int:order_id>', views.check_order_payment, name='check_order_payment'),

]