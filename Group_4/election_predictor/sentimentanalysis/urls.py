from django.urls import path
from sentimentanalysis import views

app_name = 'sentimentanalysis'
urlpatterns = [
    path('single/', views.predict_review, name='sentiment_analysis_single'),
    path('batch/', views.batch_predict, name='sentiment_analysis_batch'),
]
