from django.urls import path
from twitter_data_analysis import views

app_name = 'dataanalysis'
urlpatterns = [
    path('polarityanalysis/', views.stats, name='stats'),
    path('polarity_analysis_location/<str:location>', views.polarity_analysis_location, name='polarity_analysis_location'),
]
