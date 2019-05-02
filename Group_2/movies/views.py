from django.shortcuts import render
from .models import Movie_list
import requests

#69dfb02d97db8238985dd9d57f656946

def home(request):
    if request.method == 'POST':
        s = request.POST['search_name']
        search=str(s)
        #x='guardians of the galaxy vol. 2'
        search.replace(" ", "%20")

        response = requests.get('http://www.omdbapi.com/?t={}&apikey=769fee09'.format(search))
        geodata = response.json()
        movie = geodata['Title']
        genre = geodata['Genre']
        released = geodata['Released']
        imdb_rating = geodata['imdbRating']
        poster = geodata['Poster']
        runtime = geodata['Runtime']
        if Movie_list.objects.filter(movie = s):
            print(s)
        else:
            Movie_list.objects.create(movie=movie,genre=genre,released=released,imdb_rating=imdb_rating,poster=poster,runtime=runtime)

        return render(request,'movies/home.html', {
            'ip': geodata['Title'],
            'year':geodata['Year'],
            'genre' : geodata['Genre'],
            'released' : geodata['Released'],
            'imdbrating' : geodata['imdbRating'],
            'runtime': geodata['Runtime']

        })
    return render(request, 'movies/home.html')