from django.urls import path, include
from . import views

app_name = 'party'
urlpatterns = [
    path('', views.party, name='party'),
    path('data_analysis/', views.data_analysis, name='data_analysis'),
    path('decrease_credits/<int:amount>', views.decrease_credits, name='decrease_credits'),
    path('verify_payment/<int:credit>/', views.verify_payment, name='verify_payment'),
    path('add_payment_details/', views.payment_details, name='payment_details'),
    path('sentimentanalysis/', include('sentimentanalysis.urls')),
    path('data_analysis/', include('twitter_data_analysis.urls')),
]
