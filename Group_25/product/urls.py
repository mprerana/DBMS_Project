from django.urls import path
from product import views
app_name = 'product'

urlpatterns = [

    path('menu/', views.show_menu, name='menu'),
    path('items/<int:category_id>/', views.category_items, name='items'),
    path('add_product/', views.add_product, name='add_product')
]