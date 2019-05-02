from django.shortcuts import render
from movies.models import Movie_list
from games.models import Games_List
from tv_series.models import tv_series_list

# Create your views here.

def home(request):
    if request.method == 'POST':

        return


    return render(request, 'print/index.html')