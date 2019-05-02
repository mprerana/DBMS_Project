from django.urls import path,include, re_path
from . import views

app_name='Blood_blog'
urlpatterns = [
    path('home/',views.Home,name="home"),
    path('form/',views.DonationFormView,name="DonationFormView"),
    path('thankyou/',views.thankyou,name="Blood_blog.thankyou"),
    path('blog/',views.Blog,name="Blog"),
    path('blog/<int:pk>',views.detail,name="Blog-detail"),
    path('blog2/',views.Blog2,name="Blog2"),

]
