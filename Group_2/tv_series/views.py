from django.shortcuts import render
from .models import tv_series_list
import requests

# Create your views here.

def home(request):
    if request.method == 'POST':
        s = request.POST['search_name']
        search=str(s)
        #x='guardians of the galaxy vol. 2'
        search.replace(" ", "%20")

        response = requests.get('http://www.omdbapi.com/?t={}&apikey=769fee09'.format(search))
        geodata = response.json()
        tv_series = geodata['Title']
        genre = geodata['Genre']
        year = geodata['Year']
        released = geodata['Released']
        imdb_rating = geodata['imdbRating']
        poster = geodata['Poster']
        seasons = geodata['totalSeasons']


        if tv_series_list.objects.filter(tv_series = s):
            print(s)
        else:
            tv_series_list.objects.create(tv_series=tv_series,genre=genre,year=year,released=released,imdb_rating=imdb_rating,poster=poster,seasons=seasons)

        return render(request,'tv_series/home.html', {
            'ip': geodata['Title'],
            'year':geodata['Year'],
            'genre' : geodata['Genre'],
            'released' : geodata['Released'],
            'imdbrating' : geodata['imdbRating'],
            'seasons': geodata['totalSeasons']

        })
    return render(request, 'tv_series/home.html')