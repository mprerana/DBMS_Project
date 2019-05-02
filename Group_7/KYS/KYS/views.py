from django.shortcuts import render, get_object_or_404
from django.db import connection
from .forms import search_bar
from show.models import Show,GENRE,review,language
from cast.models import cast
from cast.models import directors as D, actors as A
from tvshow.models import TVShow as T, Season as S, Episode as E
from django.shortcuts import redirect
import csv
import datetime
from bs4 import BeautifulSoup
import requests
import random
import time
import wptools
import wikipedia
import re

def insert_data_tvshow():
    source= requests.get('https://www.imdb.com/chart/toptv/').text
    soup=BeautifulSoup(source,'lxml')
    for article in soup.find_all('td',class_='titleColumn'):
        title=article.a.text
        print(title)
        link=article.a['href']
        # print(link)
        source2= requests.get(f'https://www.imdb.com/{link}').text
        soup2=BeautifulSoup(source2,'lxml')
        genre=[]
        topbar=soup2.find('div',class_='subtext')
        for genres in topbar.find_all('a'):
            genre.append(genres.text)
        releasedate=genre[-1]
        del genre[-1]
        print(releasedate)
        print(genre)
        series_image=soup2.find('div',class_='poster').img['src']
        print(series_image)
        storyline=soup2.find('div',class_='summary_text').text
        storyline=storyline.lstrip()
        print(storyline)
        cast=[]
        # for list in soup2.find_all('div',class_='credit_summary_item'):
        #     for actors in list.find_all('a'):
        #         cast.append(actors.text)
        #         print('----------------------------------')
        #         print(BirthName)
        #         print(dob)
        #         print(placeofbirth)
        #         print(Education)
        #         print(occupation)
        #         print(Photo)
        #         print(Yearsactive)
        #         print(Biography)
        #         print('----------------------------------')
        # print(cast)
        yrs_ssn=soup2.find('div',class_='seasons-and-year-nav')
        yns=yrs_ssn.find_all('div')
        seasons=[]
        years=[]
        for season in yns[-2].find_all('a'):
            seasons.append(season.text)
        print(seasons)
        for yrs in yns[-1].find_all('a'):
            years.append(yrs.text)
        print(years)
        TV = T.objects.all()
        genres = genre
        temp_genres = GENRE.objects.all()
        GENRES = []
        for genre1 in genres:
            key_genre = False
            for i in temp_genres:
                if i.genres == genre1:
                    key_genre = True
            if not key_genre:
                GENRE.objects.create(genres=genre1)
        temp_genres = GENRE.objects.all()
        for gen in genres:
            for i in temp_genres:
                if i.genres == gen:
                    GENRES.append(i)


        temp_langs = language.objects.all()
        LANGUAGES= []
        Languages = ["English"]
        for lang in Languages:
            for i in temp_langs:
                if i.languages == lang:
                    LANGUAGES.append(i)
                    break
        key_insert_movie = True

        for i in T.objects.all():
            if i.titleName == title:
                key_insert_movie = False
        if key_insert_movie:
            instance = T(titleName=title,seriesSummary=storyline,seriesPoster=series_image)
            instance.save()
            for i in LANGUAGES:
                instance.language.add(i)
            for i in GENRES:
                instance.GENRE.add(i)
    # insert_data()
        # episodedetails=[]
        # for link2 in yns[-2].find_all('a'):
        #     link2=link2['href']
        #     source3=requests.get(f'https://www.imdb.com/{link2}').text
        #     soup3=BeautifulSoup(source3,'lxml')
        #     for list in soup3.find_all('div',class_='list_item'):
        #         try:
        #             image=list.a.img['src']
        #         except:
        #             image=None
        #         episode=list.find('div',class_=False).text
        #         reldate=list.find('div',class_='airdate').text
        #         reldate=reldate.lstrip().rstrip()
        #         episodedes=list.find('div',class_='item_description').text
        #         episodedes=episodedes.lstrip()
        #         episodetitle=list.strong.text
        #         link3=list.strong.a['href']
        #         source4=requests.get(f'https://www.imdb.com/{link3}').text
        #         soup4=BeautifulSoup(source4,'lxml')
        #         episodecast=[]
        #         for list4 in soup4.find_all('div',class_='credit_summary_item'):
        #             for actors in list4.find_all('a'):
        #                 episodecast.append(actors.text)
        #         temp1 = episode.find('S')
        #         temp2 = episode.find(',')
        #         temp3 = episode.find('p')
        #         print(episodetitle)
        #         print(image)
        #         print(episode)
        #         print(reldate)
        #         print(episodedes)
        #         print(episodecast)
        #         print()
        #         episodedetails.append([episode,episodetitle,image,reldate,episodedes])
        #         key_insert_movie = True
        #         dor = reldate.replace(".", "")
        #         for i in E.objects.all():
        #             if i.episodeName == episodetitle:
        #                 key_insert_movie = False
        #         tempo = int(episode[temp1+1:temp2])
        #         print(tempo)
        #         tempo1 = int(episode[temp3+1:])
        #         # se_num = get_object_or_404(S,seasonNum=tempo)
        #         # if not se_num:
        #             # se_num1 = S.objects.create(seasonNum=tempo)
        #         ser = get_object_or_404(T,titleName=title)
        #         runtime = random.randint(60,120)
        #         rand = random.randint(1,15)
        #         se_num = get_object_or_404(S,seasonNum=rand)
        #         if key_insert_movie:
        #             instance = E(episodeName=episodetitle,releaseDate=str(dor),episodePoster=image,season=se_num,series=ser,runTime=runtime,episodeSummary=episodedes,episodeNum=tempo1)
        #             instance.save()






def insert_data():
    source= requests.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1').text
    # count = 0
    # counter = 0
    for month in range(12,0,-1):
        # count = count + 1
        soup = BeautifulSoup(source,'lxml')
        for article in soup.find_all('div',class_='list_item'):
            title= article.h4.a.text
            genre=[]
            for item in article.p.find_all('span',class_=False):
                genre.append(item.text)
            storyline=article.find('div',class_='outline').text
            storyline=storyline.lstrip()
            Director=[]
            try:
                for director in article.find_all('div',class_='txt-block'):
                    for directors in director.find_all('a'):
                        Director.append(directors.text)
            except:
                Director=None
            image=article.img['src']
            link=article.find('div',class_='image').a['href']
            titleName = title[1:len(title)-7]
            print(titleName)
            genres = genre
            temp_genres = GENRE.objects.all()
            GENRES = []
            for genre in genres:
                key_genre = False
                for i in temp_genres:
                    if i.genres == genre:
                        key_genre = True
                if not key_genre:
                    GENRE.objects.create(genres=genre)
                    # GENRE.save()
            temp_genres = GENRE.objects.all()
            for gen in genres:
                for i in temp_genres:
                    if i.genres == gen:
                        GENRES.append(i)
            Languages = ["English"]
            LANGUAGES = []
            temp_langs = language.objects.all()
            for lang in Languages:
                key_lang = False
                # print(lang)
                for i in temp_langs:
                    if i.languages == lang:
                        key_lang = True
                if not key_lang:
                    language.objects.create(languages=lang)

            for lang in Languages:
                for i in temp_langs:
                    if i.languages == lang:
                        LANGUAGES.append(i)

            storyLine = storyline[0:len(storyline)-20]
            Directors = Director
            DIRECTORS = []
            dirs = D.objects.all()

            for dir in Directors:
                key_director = False
                for i in dirs:
                    if i.name == dir:
                        key_director = True
                if not key_director:
                    D.objects.create(name=dir)
                    break
                break
            ACTORS = []
            Actors = Directors[1:]
            acts = A.objects.all()
            for act in Actors:
                key_actor = False
                for i in acts:
                    if i.name == act:
                        key_actor = True
                if not key_actor:
                    A.objects.create(name=act)
            acts = A.objects.all()
            print(acts)
            for act in Actors:
                print(act)
                for i in acts:
                    if i.name == act:
                        print(act)
                        ACTORS.append(i)


            imageLink = image
            titlePoster1 = link
            source2=requests.get(f"https://www.imdb.com{link}").text
            soup2=BeautifulSoup(source2,'lxml')
            article2=soup2.find('div',id='titleDetails')
            dor=soup2.find('div',class_='subtext')
            dor=dor.find_all('a')[-1]
            dor=dor.text
            temp1 = dor.find('(')
            dor = dor[0:temp1-1]
            h=dor.split(" ")
            if h[1]=="January":
                h[1]="Jan"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="February":
                h[1]="Feb"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="March":
                h[1]="Mar"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="April":
                h[1]="Apr"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="June":
                h[1]="Jun"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="July":
                h[1]="Jul"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="August":
                h[1]="Aug"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="September":
                h[1]="Sep"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="October":
                h[1]="Oct"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="November":
                h[1]="Nov"
                dor = h[0]+' '+h[1]+' '+h[2]
            if h[1]=="December":
                h[1]="Dec"
                dor = h[0]+' '+h[1]+' '+h[2]
            date_time_obj = datetime.datetime.strptime(dor, '%d %b %Y')
            article2=article2.find_all('div',class_='txt-block')
            languages=[]
            for temp in article2[2].find_all('a'):
                languages.append(temp.text)
            Languages = languages
            LANGUAGES = []
            temp_langs = language.objects.all()
            for lang in Languages:
                key_lang = False
                # print(lang)
                for i in temp_langs:
                    if i.languages == lang:
                        key_lang = True
                if not key_lang:
                    language.objects.create(languages=lang)
                    # language.save()
            temp_langs = language.objects.all()
            for lang in Languages:
                for i in temp_langs:
                    if i.languages == lang:
                        LANGUAGES.append(i)
            print(Directors)

            temp_dirs = D.objects.all()
            for dir in range(0,len(Directors)):
                for i in temp_dirs:
                    # print(dir,end="")
                    # print(Directors[dir] + "----" + i.name,end=" ")
                    if i.name == Directors[dir]:
                        # print("hello")
                        DIRECTORS.append(i)
                    print()
            print("GENRES",GENRES)
            print("DIRECTORS",DIRECTORS)
            print("LANGUAGES",LANGUAGES)
            print("Actors",ACTORS)
            bud = random.randint(500,1500)
            bud = round(float(bud/11),2)
            boc = random.randint(1500,2000)
            boc = round(float(bud/11),2)
            key_insert_movie = True
            for i in Show.objects.all():
                if i.titleName == titleName:
                    key_insert_movie = False
            if key_insert_movie:
                instance = Show(titleName=titleName,releaseDate=date_time_obj,storyLine=storyLine,budget=bud,suggested_count=0,BoxOfficeCollection=boc,imageLink=imageLink)
                instance.save()
                for i in DIRECTORS:
                    instance.director.add(i)
                for i in LANGUAGES:
                    instance.language.add(i)
                for i in GENRES:
                    instance.GENRE.add(i)
                for i in ACTORS:
                    instance.cast.add(i)

            # instance.cast.add(GENRES)
            # break
        source=requests.get(f"https://www.imdb.com/movies-coming-soon/2018-{month}").text
    insert_data_tvshow()



def mainpage(request):
    # insert_data()
    list_of_movies=[]
    movies = Show.objects.raw('''
        SELECT * FROM show_show;
    ''')

    list_of_movies.append(["Movies",movies])
    movies_telugu = Show.objects.raw('''
        SELECT * FROM show_show
        WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages="Telugu"));
        ;
    ''')
    tvshows = T.objects.raw('''
        SELECT * FROM tvshow_tvshow;
    ''')
    list_of_movies.append(["Telugu Movies", movies_telugu])
    movies_english = Show.objects.raw('''
        SELECT * FROM show_show
        WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages="English"));
        ;
    ''')

    list_of_movies.append(["Engish Movies", movies_english])
    movies_tamil = Show.objects.raw('''
            SELECT * FROM show_show
            WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages="Tamil"));
            ;
        ''')

    list_of_movies.append(["Tamil Movies", movies_tamil])
    movies_malyalam = Show.objects.raw('''
                SELECT * FROM show_show
                WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages="Malyalam"));
                ;
            ''')

    list_of_movies.append(["Malyalam Movies", movies_malyalam])
    movies_hindi = Show.objects.raw('''
                    SELECT * FROM show_show
                    WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages="Hindi"));
                    ;
                ''')

    list_of_movies.append(["Hindi Movies", movies_hindi])
    movies_horror = Show.objects.raw('''
                        select * from show_show where id in(select show_id from show_show_genre where genre_id in (select id from show_genre where genres="Horror"));
                        ;
                    ''')

    list_of_movies.append(["Horror Movies", movies_horror])
    movies_comedy = Show.objects.raw('''
                            select * from show_show where id in(select show_id from show_show_genre where genre_id in (select id from show_genre where genres="Comedy"));
                            ;
                        ''')

    list_of_movies.append(["Comedy Movies", movies_comedy])
    movies_suspense= Show.objects.raw('''
                                select * from show_show where id in(select show_id from show_show_genre where genre_id in (select id from show_genre where genres="Suspense"));
                                ;
                            ''')

    list_of_movies.append(["Suspense Movies", movies_suspense])
    movies_thriller = Show.objects.raw('''
                                select * from show_show where id in(select show_id from show_show_genre where genre_id in (select id from show_genre where genres="Thriller"));
                                ;
                            ''')

    list_of_movies.append(["Thriller Movies", movies_thriller])
    movies_drama = Show.objects.raw('''
                                select * from show_show where id in(select show_id from show_show_genre where genre_id in (select id from show_genre where genres="Drama"));
                                ;
                            ''')

    list_of_movies.append(["Drama Movies", movies_drama])
    form = search_bar()

    context = {
        # 'search_form':form,
        'movies':movies,
        # 'movies_telugu':movies_telugu,
        # 'movies_english':movies_english,
        # 'movies_tamil': movies_tamil,
        # 'movies_malyalam': movies_malyalam,
        # 'movies_hindi': movies_hindi,
        # 'movies_horror':movies_horror,
        'search_form':form,
        'list_of_movies':list_of_movies,
        'tvshows':tvshows,
    }

    return render(request,'KYS/homePage.html',context)


def search(request):
    if request.method == 'POST':
        form = search_bar(request.POST)
        if form.is_valid():
            search_list = ['titleName', 'storyLine']
            search_query = form.cleaned_data['search_query']
            search_ty = form.cleaned_data['search_ty']
            all_searches = []
            if search_ty == 'Movies':
                all_shows_with_query = Show.objects.raw('''
                               SELECT *, EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,titleName)
                               FROM show_show
                               WHERE locate(%s,titleName)>0;
                   ''', [search_query, search_query])

                for i in all_shows_with_query:
                    all_searches.append(i)

                all_shows_with_query1 = Show.objects.raw('''
                           SELECT *, EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,storyLine)
                           FROM show_show
                           WHERE locate(%s,storyLine)>0;
                   ''', [search_query, search_query])
                for i in all_shows_with_query1:
                    all_searches.append(i)

                all_searches = set(all_searches)

                for i in all_searches:
                    print(i)

                if all_searches:
                    key=True

                else:
                    key=False
                form=search_bar()
                context = {
                              'all_searches': all_searches, 'key': key,
                    'search_query': search_query,
                    'search_form':form
                }
                return render(request, 'KYS/search_result.html', context)

            elif search_ty == 'Cast':
                all_shows_with_query = cast.objects.raw('''
                               SELECT *, LOCATE(%s,name)
                               FROM cast_actors
                               WHERE locate(%s,name)>0;
                   ''', [search_query, search_query])

                for i in all_shows_with_query:
                    print(i, ' hello')

                if all_shows_with_query:
                    key=True
                else:
                    key=False
                print(search_query)
                form=search_bar()
                context = {
                    'all_shows_with_query': all_shows_with_query,
                    'key':key,
                    'search_query' : search_query,
                    'search_form':form,
                }
                return render(request, 'KYS/search_result.html', context)
            elif search_ty == "Tv shows":
                all_shows_with_query_TV = T.objects.raw('''
                        SELECT *,lOCATE(%s,titleName)
                        FROM tvshow_tvshow
                        WHERE locate(%s,titleName)>0;
                ''',[search_query, search_query])
                for i in all_shows_with_query_TV:
                    print(i, ' hello')

                if all_shows_with_query_TV:
                    key=True
                else:
                    key=False
                print(search_query)
                form=search_bar()
                context = {
                    'all_shows_with_query_TV': all_shows_with_query_TV,
                    'key':key,
                    'search_query' : search_query,
                    'search_form':form,
                }
                return render(request, 'KYS/search_result.html', context)
    form = search_bar()
    context = {
        'search_form':form,
    }
    return render(request,'KYS/homePage.html',context)
