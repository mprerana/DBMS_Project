from django.shortcuts import render
from django.db import connection
from KYS.forms import search_bar
from show.models import Show
from show.models import language
from .models import cast
from bs4 import BeautifulSoup
import requests
import wptools
import wikipedia
import re
# Create your views here.

def Cast(request,id):
    if request.method == 'POST':
        form = search_bar(request.POST)
        if form.is_valid():
            search_list =  ['titleName','storyLine']
            search_query = form.cleaned_data['search_query']
            search_ty = form.cleaned_data['search_ty']
            all_searches = []
            if search_ty == 'movies':
                all_shows_with_query = Show.objects.raw('''
                            SELECT * , EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,titleName)
                            FROM show_show
                            WHERE locate(%s,titleName)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    all_searches.append(i)


                all_shows_with_query1 = Show.objects.raw('''
                        SELECT * , EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,storyLine)
                        FROM show_show
                        WHERE locate(%s,storyLine)>0;
                ''',[search_query,search_query])
                for i in all_shows_with_query1:
                    all_searches.append(i)

                all_searches = set(all_searches)


                for i in all_searches:
                    print(i)
            elif search_ty == 'All':
                all_shows_with_query = Show.objects.raw('''
                            SELECT * , EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,titleName)
                            FROM show_show
                            WHERE locate(%s,titleName)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    all_searches.append(i)


                all_shows_with_query1 = Show.objects.raw('''
                        SELECT * , EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,storyLine)
                        FROM show_show
                        WHERE locate(%s,storyLine)>0;
                ''',[search_query,search_query])
                for i in all_shows_with_query1:
                    all_searches.append(i)

                all_searches = set(all_searches)

                all_shows_with_query = cast.objects.raw('''
                            SELECT *, LOCATE(%s,name)
                            FROM cast_cast
                            WHERE locate(%s,name)>0;
                ''',[search_query,search_query])
                for i in all_searches:
                    print(i)
            else:
                all_shows_with_query = cast.objects.raw('''
                            SELECT *, LOCATE(%s,name)
                            FROM cast_cast
                            WHERE locate(%s,name)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    print(i)
    actor = cast.objects.raw('''
        SELECT * FROM cast_cast
        WHERE id=%s
        ;
    ''',[id,])
    castActedMovies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in (SELECT show_id FROM show_show_cast WHERE cast_id=%s)
        ORDER BY releaseDate DESC;
    ''',[id])
    castProfession = cast.objects.raw('''
        SELECT * FROM cast_profession
        where id in (select profession_id from cast_cast_profession where cast_id=%s);
    ''',[id])
    form = search_bar()
    for i in castActedMovies:
        yearStarted = i.year
    context = {
        'Cast':actor[0],
        'search_form':form,
        'moviesActed':castActedMovies,
        'castProfession':castProfession,
        'yearStarted' : yearStarted,
    }
    return render(request,'cast/cast.html',context)


def Director(request,id):
    if request.method == 'POST':
        form = search_bar(request.POST)
        if form.is_valid():
            search_list =  ['titleName','storyLine']
            search_query = form.cleaned_data['search_query']
            search_ty = form.cleaned_data['search_ty']
            all_searches = []
            if search_ty == 'movies':
                all_shows_with_query = Show.objects.raw('''
                            SELECT *, LOCATE(%s,titleName)
                            FROM show_show
                            WHERE locate(%s,titleName)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    all_searches.append(i)


                all_shows_with_query1 = Show.objects.raw('''
                        SELECT * , LOCATE(%s,storyLine)
                        FROM show_show
                        WHERE locate(%s,storyLine)>0;
                ''',[search_query,search_query])
                for i in all_shows_with_query1:
                    all_searches.append(i)

                all_searches = set(all_searches)


                for i in all_searches:
                    print(i)
            else:
                all_shows_with_query = cast.objects.raw('''
                            SELECT *, LOCATE(%s,name)
                            FROM cast_cast
                            WHERE locate(%s,name)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    print(i)
    director = cast.objects.raw('''
        SELECT * FROM cast_directors
        WHERE id=%s;
    ''',[id])
    # castProfession = cast.objects.raw('''
    #     SELECT * FROM cast_profession
    #     where id in (select profession_id from cast_director_profession where director_id=%s);
    # ''',[id])
    directedMovies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in (SELECT show_id FROM show_show_director WHERE directors_id=%s)
        ORDER BY releaseDate DESC;
    ''',[id])
    form = search_bar()
    for i in directedMovies:
        yearStarted = i.year
    context = {
        'crew' : director[0],
        'crewMovies': directedMovies,
        # 'castProfession':castProfession,
        'key' : True,
        'yearStarted' : yearStarted,
    }
    return render(request,'cast/crew.html',context)


def Producer(request,id):
    if request.method == 'POST':
        form = search_bar(request.POST)
        if form.is_valid():
            search_list =  ['titleName','storyLine']
            search_query = form.cleaned_data['search_query']
            search_ty = form.cleaned_data['search_ty']
            all_searches = []
            if search_ty == 'movies':
                all_shows_with_query = Show.objects.raw('''
                            SELECT *, LOCATE(%s,titleName)
                            FROM show_show
                            WHERE locate(%s,titleName)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    all_searches.append(i)


                all_shows_with_query1 = Show.objects.raw('''
                        SELECT * , LOCATE(%s,storyLine)
                        FROM show_show
                        WHERE locate(%s,storyLine)>0;
                ''',[search_query,search_query])
                for i in all_shows_with_query1:
                    all_searches.append(i)

                all_searches = set(all_searches)


                for i in all_searches:
                    print(i)
            else:
                all_shows_with_query = cast.objects.raw('''
                            SELECT id,name , LOCATE(%s,name)
                            FROM cast_cast
                            WHERE locate(%s,name)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    print(i)

    castProfession = cast.objects.raw('''
        SELECT * FROM cast_profession
        where id in (select profession_id from cast_producer_profession where producer_id=%s);
    ''',[id])
    producer = cast.objects.raw('''
        SELECT * FROM cast_producer
        WHERE id=%s;
    ''',[id])
    producedMovies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in (SELECT show_id FROM show_show_producer WHERE producer_id=%s)
        ORDER BY releaseDate DESC;
    ''',[id])
    for i in producedMovies:
        yearStarted = i.year
    form = search_bar()
    context = {
        'crew' : producer[0],
        'crewMovies': producedMovies,
        'yearStarted' : yearStarted,
        'key' : True,
    }
    return render(request,'cast/crew.html',context)



def cast_details(request,id):
    Name = cast.objects.raw('''
        SELECT * FROM cast_directors
        WHERE id = %s;
    ''',[id])
    name = Name[0].name
    cast_data = wptools.page(name).get_parse()
    infobox = cast_data.data['infobox']
    try:
        BirthName= infobox['birth_name']
    except:
        BirthName=None
    try:
        a = re.split('[{{ | }}]' , infobox['birth_date'])
        dob = []
        for i in a:
            try:
                dob.append(int(i))
            except:
                pass
    except:
        dob = None
    try:
        s = infobox['birth_place']
        placeofbirth = ''.join(i for i in s if i not in [ '[' , ']' ])
    except:
        placeofbirth=None
    try:
        s1= infobox['education']
        Education = ''.join(i for i in s1 if i not in [ '[' , ']', '(', ')' ])
    except:
        try:
            s1= infobox['alma_mater']
            Education = ''.join(i for i in s1 if i not in [ '[' , ']', '(', ')' ])
        except:
            Education= None
    try:
        s1= infobox['occupation']
        s2 = ''.join(i for i in s1 if i not in [ '[' , ']', '(', ')', '{', '}' ])
        s2 = re.split('[\n* , |]', s2)
        occupation = [x for x in s2 if x != '']
        if occupation[0] == 'flatlist':
            occupation.remove('flatlist')
        if occupation[0] == 'hlist':
            occupation.remove('hlist')
    except:
        occupation = None
    try:
        Photo = cast_data.data['image'][0]['url']
    except:
        Photo = None
    try:
        Yearsactive = infobox['years_active']
    except:
        Yearsactive = None
    Biography= wikipedia.page(name).summary

    details = {
        'name':name,
        'BirthName':BirthName,
        'dob':dob,
        'placeofbirth':placeofbirth,
        'Education':Education,
        'Photo':Photo,
        'Yearsactive':Yearsactive,
        'Biography':Biography,
    }
    return render(request,'cast/crew.html',details)

def CAST(request,id):
    Name = cast.objects.raw('''
        SELECT * FROM cast_actors
        WHERE id = %s;
    ''',[id])
    name = Name[0].name

    cast_data = wptools.page(name).get_parse()
    infobox = cast_data.data['infobox']
    try:
        BirthName = infobox['birth_name']
    except:
        BirthName = None
    try:
        a = re.split('[{{ | }}]' , infobox['birth_date'])
        dob = []
        for i in a:
            try:
                dob.append(int(i))
            except:
                pass
    except:
        dob = None
    try:
        s = infobox['birth_place']
        placeofbirth = ''.join(i for i in s if i not in [ '[' , ']' ])
    except:
        placeofbirth = None
    try:
        s1= infobox['education']
        Education = ''.join(i for i in s1 if i not in [ '[' , ']', '(', ')' ])
    except:
        try:
            s1= infobox['alma_mater']
            Education = ''.join(i for i in s1 if i not in [ '[' , ']', '(', ')' ])
        except:
            Education = None
    try:
        s1= infobox['occupation']
        s2 = ''.join(i for i in s1 if i not in [ '[' , ']', '(', ')', '{', '}' ])
        s2 = re.split('[\n* , |]', s2)
        occupation = [x for x in s2 if x != '']
        if occupation[0] == 'flatlist':
            occupation.remove('flatlist')
        if occupation[0] == 'hlist':
            occupation.remove('hlist')
    except:
        occupation = None
    try:
        Photo = cast_data.data['image'][0]['url']
    except:
        Photo = None
    try:
        Yearsactive = infobox['years_active']
    except:
        Yearsactive = None
    Biography= wikipedia.page(name).summary

    details = {
        'name':name,
        'BirthName':BirthName,
        'dob':dob,
        'placeofbirth':placeofbirth,
        'Education':Education,
        'Photo':Photo,
        'Yearsactive':Yearsactive,
        'Biography':Biography,
    }
    return render(request,'cast/crew.html',details)
