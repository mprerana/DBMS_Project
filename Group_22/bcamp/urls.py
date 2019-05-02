from django.urls import path
from . import views as BCampviews
# from . import views

app_name='bcamp'

urlpatterns = [

    path('BcampHome/', BCampviews.BcampList, name='BcampHome'),
    path('CampForm/',BCampviews.CampFormView, name ='BloodCampForm'),
    path('NewVol/',BCampviews.NewVolForm, name='NewVolForm'),
    path('NewCamp/',BCampviews.NewCampForm, name='NewCamp'),
]
