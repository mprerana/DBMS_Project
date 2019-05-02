from django.shortcuts import render
from django.db import connection
import csv

# Create your views here.


def populating_movies(request):

   # Populating movies table
    print("populating data.....")
    with connection.cursor() as cursor:

        #Inserting Movies
        movies=open('movies\Dbms_pro\movies.csv','r')
        movie_reader=csv.reader(movies)

        already_inserted_movie=[]

        for line in movie_reader:
            if(line[0] not in already_inserted_movie):
                print(line[0])
                cursor.execute(''' insert ignore into movies_movies(title,release_date,censor_rating,image_source,synopsis,trailer_link,time_duration,likes,status) values( %s,%s,%s,%s,%s,%s,%s,%s,%s)  ''',[line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8]])
                already_inserted_movie.append(line[0])

        movies.close()

        print("Movies_table filled...")

        #populating cast crew
        cast_crew_file=open('movies\Dbms_pro\current_movies_cast_crew.csv','r')
        cast_crew_reader=csv.reader(cast_crew_file)
        cast_crew=[]
        for line in cast_crew_reader:
            if line[1] not in cast_crew:
                cast_crew.append(line[1])
                cursor.execute(''' insert ignore into movies_cast_crew(castname,image) values( %s , %s )  ''',[line[1],line[2]])

        cast_crew_file.close()

        #cast_crew_movie
        cast_crew_file=open('movies\Dbms_pro\current_movies_cast_crew.csv','r')
        cast_crew_reader=csv.reader(cast_crew_file)

        cursor.execute(''' select * from movies_movies ''')
        movies_list=cursor.fetchall()

        cursor.execute(''' select * from movies_cast_crew ''')
        cast_list = cursor.fetchall()

        cast_crew_movie=[]
        for line in cast_crew_reader:
            for i in range(0,len(movies_list)):
                if(line[0] == movies_list[i][1]):
                    title_id=movies_list[i][0]
                    break

            for j in range(0,len(cast_list)):
                if(line[1]==cast_list[j][1]):
                    cast_id=cast_list[j][0]
                    break

            a=str(title_id)+str(cast_id)
            if a not in cast_crew_movie:
                cast_crew_movie.append(a)
                cursor.execute(''' insert ignore into movies_cast_crew_movie(cast_crew_id,title_id) values( %s , %s )  ''',[cast_id,title_id])

        cast_crew_file.close()

        print("Cast_crew_completed.....")

        #Populating languages
        languages=open('movies\Dbms_pro\movie_language.csv','r')
        language_reader=csv.reader(languages)

        already_inserted_languages=[]

        lang_list=[]
        for line in language_reader:
            lang_list.append(line[1])

        for lang in lang_list:
            if( lang not in already_inserted_languages  ):
                cursor.execute(''' insert ignore into movies_languages(language) values(%s)  ''',[lang])
                already_inserted_languages.append(lang)

        languages.close()

        #Language_movie model
        languages=open('movies\Dbms_pro\movie_language.csv','r')
        language_reader=csv.reader(languages)

        movie_language=[]
        cursor.execute(''' select * from movies_movies ''')
        movies_list=cursor.fetchall()

        cursor.execute(''' select * from movies_languages ''')
        languages_list=cursor.fetchall()

        for line in language_reader:
            for i in range(0,len(movies_list)):
                if(line[0]==movies_list[i][1]):
                    title_id=movies_list[i][0]
                    break

            for j in range(0,len(languages_list)):
                if(line[1]==languages_list[j][1]):
                    lg_id=languages_list[j][0]
                    break
            a=str(title_id)+str(lg_id)
            if a not in movie_language:
                movie_language.append(a)
                cursor.execute(''' insert ignore into movies_language_movie(movie_language_id,title_id) values( %s , %s )  ''',[lg_id,title_id])

        languages.close()
        print("Languages_completed.....")

        ##Populating movie_formats
        formats=open('movies\Dbms_pro\movie_format.csv','r')
        format_reader=csv.reader(formats)

        already_inserted_formats=[]

        format_list=[]
        for form in format_reader:
            format_list.append(form[1])

        for form in format_list:
            if( form not in already_inserted_formats ):
                cursor.execute(''' insert ignore into movies_formats(mformat) values(%s)  ''',[form])
                already_inserted_formats.append(form)

        formats.close()

        #Format_movie model
        formats=open('movies\Dbms_pro\movie_format.csv','r')
        format_reader=csv.reader(formats)
        movie_format=[]

        cursor.execute(''' select * from movies_movies ''')
        movies_list=cursor.fetchall()

        cursor.execute(''' select * from movies_formats ''')
        format_list=cursor.fetchall()

        for line in format_reader:
            for i in range(0,len(movies_list)):
                if(line[0] == movies_list[i][1]):
                    title_id=movies_list[i][0]
                    break

            for j in range(0,len(format_list)):
                if(line[1]==format_list[j][1]):
                    fr_id=format_list[j][0]
                    break

            a=str(title_id)+str(fr_id)
            if a not in movie_format:
                movie_format.append(a)
                cursor.execute(''' insert ignore into movies_format_movie(movie_format_id,title_id) values( %s , %s )  ''',[fr_id,title_id])

        formats.close()

        print("Format_completed....")

        ##Populating genre
        genres=open('movies\Dbms_pro\movie_genre.csv','r')
        genre_reader=csv.reader(genres)

        already_inserted_genres=[]

        genre_list=[]
        for line in genre_reader:
            genre_list.append(line[1].strip())

        for gen in genre_list:
            if( gen.strip() not in already_inserted_genres  ):
                cursor.execute(''' insert ignore into movies_genre(genre) values(%s)  ''',[gen])
                already_inserted_genres.append(gen)

        genres.close()

        ##populating genre_movie
        genres=open('movies\Dbms_pro\movie_genre.csv','r')
        genre_reader=csv.reader(genres)
        gen_movie=[]
        cursor.execute(''' select * from movies_movies ''')
        movies_list=cursor.fetchall()

        cursor.execute(''' select * from movies_genre ''')
        genre_list=cursor.fetchall()

        for line in genre_reader:
            for i in range(0,len(movies_list)):
                if(line[0] == movies_list[i][1]):
                    title_id=movies_list[i][0]
                    break

            for j in range(0,len(genre_list)):
                if(line[1].strip()==genre_list[j][1]):
                    gen_id=genre_list[j][0]
                    break
            a=str(title_id)+str(gen_id)
            if a not in gen_movie:
                gen_movie.append(a)
                cursor.execute(''' insert ignore into movies_genre_movie(movie_genre_id,title_id) values( %s , %s )  ''',[gen_id,title_id])

        genres.close()

        print("Genre_completed......")

        #Populating  City_Theatre model

        theatre_city=open('movies\Dbms_pro\city_theatres.csv','r')
        theatre_reader=csv.reader(theatre_city)
        citytheatre=[]
        for line in theatre_reader:
            if line not in citytheatre and line!=[]:
                citytheatre.append(line)

        cursor.execute(''' select * from movies_cities ''')
        city_list=cursor.fetchall()

        for line in citytheatre:
            for i in range(0,len(city_list)):
                if(line[0] == city_list[i][1].lower()):
                    city_id = city_list[i][0]
                    break

            theatre_name=line[1]
            print(theatre_name,city_id)
            cursor.execute(''' insert ignore into movies_city_theatre(theatre_name,city_id) values( %s , %s )  ''',[theatre_name,city_id])

        theatre_city.close()

        print("city_theatre_completed......")

        ##populating city_movie
        city_movie1=[]
        city_movie=open('movies\Dbms_pro\movies_cities.csv','r')
        citymovie=csv.reader(city_movie)

        cursor.execute(''' select * from movies_movies ''')
        movies_list=cursor.fetchall()

        cursor.execute(''' select * from movies_cities ''')
        city_list=cursor.fetchall()

        for line in citymovie:
            for i in range(0,len(movies_list)):
                if(line[1] == movies_list[i][1]):
                    title_id=movies_list[i][0]
                    break

            for j in range(0,len(city_list)):

                if(line[0]==city_list[j][1].lower()):

                    cr_id=city_list[j][0]
                    break

            a=str(title_id)+str(cr_id)

            if a not in city_movie1:
                city_movie1.append(a)
                cursor.execute(''' insert ignore into movies_city_movie(city_id,movie_title_id) values( %s , %s )  ''',[cr_id,title_id])

        city_movie.close()
        print("city_movie_completed......")

        # populating  theatre_showtimings
        theatre_showtimings = open(
            'movies\Dbms_pro\\theatre_showtimings.csv', 'r')
        theatre_show = csv.reader(theatre_showtimings)

        movies = []

        cursor.execute(''' select * from movies_city_theatre ''')
        city_theatre_list = cursor.fetchall()

        cursor.execute(''' select * from movies_movies ''')
        movie_list = cursor.fetchall()

        cursor.execute(''' select * from movies_formats ''')
        format_list = cursor.fetchall()

        cursor.execute(''' select * from movies_languages ''')
        language_list = cursor.fetchall()

        cursor.execute(''' select * from movies_cities ''')
        city_list = cursor.fetchall()

        for line in theatre_show:

            for i in range(0, len(movie_list)):
                if(line[4] == movie_list[i][1]):
                    title_id = movie_list[i][0]
                    break

            for i in range(0, len(format_list)):
                if(line[6] == format_list[i][1]):
                    format_id = format_list[i][0]
                    break

            for i in range(0, len(language_list)):
                if(line[5] == language_list[i][1]):
                    language_id = language_list[i][0]
                    break

            show_timings = line[7]
            date = line[3]

            for i in range(0, len(city_list)):
                if(line[0] == city_list[i][1].lower()):
                    city_id = city_list[i][0]
                    break

            for i in range(0, len(city_theatre_list)):

                if(city_id == city_theatre_list[i][2] and line[1] == city_theatre_list[i][1]):
                    citytheatre_id = city_theatre_list[i][0]

                    break

            cursor.execute(''' insert ignore into movies_theatre_showtimings(citytheatre_id,date,title_id,language_id,format_id,show_timings) values( %s , %s , %s , %s , %s , %s )  ''', [
                           citytheatre_id, date, title_id, language_id, format_id, show_timings])

        theatre_showtimings.close()

        print("theatre_showtime_completed......")

       # Populating reviews
        reviews_file = open('movies\Dbms_pro\movie_reviews.csv', 'r')
        reviews_reader = csv.reader(reviews_file)

        cursor.execute(''' select * from movies_movies ''')
        movie_list = cursor.fetchall()

        cursor.execute(''' select * from auth_user ''')
        user_list = cursor.fetchall()

        movie_list12 = []

        likestatus = True
        ratestatus = True

        user_id = 1
        for line in reviews_reader:
            if(line[0] not in movie_list12):
                movie_list12.append(line[0])
                user_id = 1

            for i in range(0, len(movie_list)):
                if(line[0] == movie_list[i][1]):
                    movie_id = movie_list[i][0]
                    break

            print(user_id, line[0])

            cursor.execute(''' insert ignore into movies_rating(title_id,user_id,ratestatus,rating,comment) values( %s , %s , %s , %s , %s )  ''', [
                           movie_id, user_id, ratestatus, line[2], line[1]])

            user_id = user_id+1

        reviews_file.close()

    return render(request, 'index.html')
