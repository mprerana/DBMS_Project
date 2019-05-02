from django import forms
from django.db import connection
from show.models import Show, GENRE, review, language
from cast.models import cast
from cast.models import directors as D
import csv
import datetime
from bs4 import BeautifulSoup
import requests
import random

def insert_data():
    source= requests.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1').text
    count = 0
    counter = 0
    for month in range(12,0,-1):
        count = count + 1
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
            print()
            print()

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
                    # D.save()
            counter = counter+1

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
                    print(dir,end="")
                    print(Directors[dir] + "----" + i.name,end=" ")
                    if i.name == Directors[dir]:
                        print("hello")
                        DIRECTORS.append(i)
                    print()
            print("GENRES",GENRES)
            print("DIRECTORS",DIRECTORS)
            print("LANGUAGES",LANGUAGES)
            bud = random.randint(500,1500)
            bud = round(float(bud/11),2)
            boc = random.randint(1500,2000)
            boc = round(float(bud/11),2)
            instance = Show(titleName=titleName,releaseDate=date_time_obj,storyLine=storyLine,budget=bud,suggested_count=0,BoxOfficeCollection=boc,imageLink=imageLink)
            instance.save()
            for i in DIRECTORS:
                instance.director.add(i)
            for i in LANGUAGES:
                instance.language.add(i)
            for i in GENRES:
                instance.GENRE.add(i)
            # instance.cast.add(GENRES)
            break

        source=requests.get(f"https://www.imdb.com/movies-coming-soon/2018-{month}").text

insert_data()
