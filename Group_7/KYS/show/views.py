from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .forms import genreForm,languageForm,show_update_form
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import language
from KYS.forms import search_bar
from show.models import Show
from cast.models import cast

# Create your views here.
def get_suggested_movies(id):
    langs = Show.objects.raw('''
        SELECT * FROM show_language
        WHERE id in (SELECT language_id FROM show_show_language WHERE show_id=%s);
        ;
    ''',[id])
    genres = Show.objects.raw('''
        SELECT * FROM show_GENRE
        WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s);
        ;
    ''',[id])
    # directors = cast.objects.raw('''
    #     SELECT * FROM cast_director
    #     WHERE id in (SELECT director_id FROM show_show_director WHERE show_id=%s);
    # ''',[id])
    # producers = cast.objects.raw('''
    #     SELECT * FROM cast_producer
    #     WHERE id in (SELECT producer_id FROM show_show_producer WHERE show_id=%s);
    # ''',[id])
    suggested_movies_genre = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in ((SELECT show_id FROM show_show_GENRE WHERE genre_id in (SELECT id FROM show_GENRE WHERE genres in
        (SELECT genres FROM show_GENRE WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s))
        )));
    ''',[id])
    suggested_movies_lang = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages in
        (SELECT languages FROM show_language WHERE id in (SELECT  language_id FROM show_show_language WHERE show_id=%s))
        ))
        ORDER BY suggested_count DESC;
    ''',[id])
    shows = Show.objects.raw('''
        SELECT * FROM show_show;
    ''')
    # for temp in shows:
    #     with connection.cursor() as cursor:
    #         cursor.execute('''
    #             UPDATE show_show
    #             SET suggested_count = 0
    #             WHERE id=%s;
    #         ''',[temp.id])
    # for movie_temp in suggested_movies_lang:
    #     lang_movie_temp = Show.objects.raw('''
    #         SELECT * FROM show_language
    #         WHERE id in (SELECT language_id FROM show_show_language WHERE show_id=%s);
    #     ''',[movie_temp.id])
    #     # for i in lang_movie_temp:
    #     #     print(i.languages)
    #     #     print()
    #     # lang_movie_temp = []
    #     count = movie_temp.suggested_count
    #     for lang_temp in langs:
    #         for temp_lang in lang_movie_temp:
    #             if(lang_temp.languages==temp_lang.languages):
    #                 count = count + 1
    #     with connection.cursor() as cursor:
    #         cursor.execute('''
    #             UPDATE show_show
    #             SET suggested_count = %s
    #             WHERE id=%s;
    #         ''',[count,movie_temp.id])



    # for movie_temp in suggested_movies_genre:
    #     genres_movie_temp = Show.objects.raw('''
    #         SELECT * FROM show_GENRE
    #         WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s);
    #         ;
    #     ''',[movie_temp.id])
    #     count = movie_temp.suggested_count
    #     for genre_temp in genres:
    #         for temp_genre in genres_movie_temp:
    #             if(genre_temp.genres==temp_genre.genres):
    #                 count = count + 1
    #     # print(movie_temp.suggested_count)
    #     with connection.cursor() as cursor:
    #         cursor.execute('''
    #             UPDATE show_show
    #             SET suggested_count = %s
    #             WHERE id=%s;
    #         ''',[count,movie_temp.id])



    suggested_movies_lang = Show.objects.raw('''
        SELECT id,titleName,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in (SELECT show_id FROM show_show_language WHERE language_id in (SELECT id FROM show_language WHERE languages in
        (SELECT languages FROM show_language WHERE id in (SELECT  language_id FROM show_show_language WHERE show_id=%s))
        ))
        ORDER BY suggested_count DESC;
    ''',[id])
    suggested_movies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE suggested_count!=0;
    ''')
    # for i in suggested_movies:
    #     print(i.titleName)
    #     print(i.suggested_count)
    # print()
    # for i in suggested_movies_genre:
    #     print(i.suggested_count)
    print()
    print()
    return suggested_movies_genre


def movie(request,id):
    user_rated = True
    user_review = Show.objects.raw('''
        SELECT * FROM show_review
        WHERE reviewer_id=%s AND show_id=%s;
    ''',[request.user.id,id])
    if not len(user_review):
        user_rated = False
    if request.method == 'POST':
        form = search_bar(request.POST)
        if form.is_valid():
            search_list =  ['titleName','storyLine']
            search_query = form.cleaned_data['search_query']
            search_ty = form.cleaned_data['search_ty']
            all_searches = []
            if search_ty == 'movies':
                all_shows_with_query = Show.objects.raw('''
                            SELECT *,EXTRACT(YEAR FROM releaseDate) AS year, LOCATE(%s,titleName)
                            FROM show_show
                            WHERE locate(%s,titleName)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    all_searches.append(i)


                all_shows_with_query1 = Show.objects.raw('''
                        SELECT *, EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,storyLine)
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
                            SELECT *, EXTRACT(YEAR FROM releaseDate) AS year,LOCATE(%s,name)
                            FROM cast_cast
                            WHERE locate(%s,name)>0;
                ''',[search_query,search_query])

                for i in all_shows_with_query:
                    print(i)
    movies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id=%s
        ;
    ''',[id,])
    form = search_bar()
    castActed = Show.objects.raw('''
        SELECT * FROM cast_actors
        WHERE id in (SELECT actors_id FROM show_show_cast WHERE show_id=%s);
        ;
    ''',[id])
    langs = Show.objects.raw('''
        SELECT * FROM show_language
        WHERE id in (SELECT language_id FROM show_show_language WHERE show_id=%s);
        ;
    ''',[id])
    genres = Show.objects.raw('''
        SELECT * FROM show_GENRE
        WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s);
        ;
    ''',[id])
    directors = cast.objects.raw('''
        SELECT * FROM cast_directors
        WHERE id in (SELECT directors_id FROM show_show_director WHERE show_id=%s);
    ''',[id])
    reviews = Show.objects.raw('''
        SELECT *,username FROM show_review,auth_user
        WHERE show_review.show_id = %s AND show_review.reviewer_id = auth_user.id
        ORDER BY date_reviewed;
    ''',[id])
    avgRating =Show.objects.raw('''
        SELECT id,AVG(rating) AS KYSavg,COUNT(*) AS total FROM show_review
        WHERE show_id = %s;
    ''',[id])
    currentUser_review = Show.objects.raw('''
        SELECT *,username FROM show_review,auth_user
        WHERE show_review.show_id = %s AND show_review.reviewer_id = auth_user.id AND show_review.reviewer_id=%s;
    ''',[id,request.user.id])
    KYS_suggested_movies = Show.objects.raw('''
        SELECT id,show_id,AVG(rating) AS KYSavg FROM show_review GROUP BY show_id ORDER BY KYSavg DESC;
    ''')
    KYS_suggest = []
    all_movies =  Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show;
    ''')
    for i in KYS_suggested_movies:
        for j in all_movies:
            print(i.show_id,j.id)
            if i.show_id == j.id:
                KYS_suggest.append(j)
                break
    print(KYS_suggest)
    for i in KYS_suggest:
        print(i.titleName)
    suggested_movies = get_suggested_movies(id)
    # suggested_movies = []
    # for i in suggested_movies_genre:
    #     suggested_movies[i]
        # print(genre_temp.genres)
    if reviews:
        RATING_INFO = True
        total_rating = round(avgRating[0].KYSavg,2)
    else:
        RATING_INFO = False
        total_rating = 0

    if not currentUser_review:
        context = {
            'show':movies[0],
            'search_form':form,
            'cast':castActed,
            'Genres' : genres,
            'Languages':langs,
            'reviews':reviews,
            'Directors':directors,
            'total_reviews':len(reviews),
            'user_rated':user_rated,
            'RATING_INFO': RATING_INFO,
            'KYSrating':total_rating,
            'KYS_suggested_movies':KYS_suggest,
            'suggested_movies':suggested_movies,
        }
    else:

        context = {
            'show':movies[0],
            'search_form':form,
            'cast':castActed,
            'Genres' : genres,
            'Languages':langs,
            'reviews':reviews,
            'Directors':directors,
            'user_rated':user_rated,
            'total_reviews':len(reviews),
            'currentUser_review':currentUser_review[0],
            'RATING_INFO': RATING_INFO,
            'KYSrating': total_rating,
            'KYS_suggested_movies':KYS_suggest,
            'suggested_movies':suggested_movies,
        }
    # with connection.cursor() as cursor:
    #     cursor.execute('''
    #         CALL update_movie_count(@%s);
    #     ''',[id])
    # with connection.cursor() as cursor:
    #     cursor.execute('''
    #         UPDATE show_show
    #         SET movieViewCount = movieViewCount + 1
    #         WHERE movie_id = %s;
    #     ''',[id])
    # a = Show.objects.get(pk=id)
    # print(a.count)
    return render(request,'show/movie.html',context)


@login_required(login_url='/accounts/login/')
def review_rate(request,id):
    if request.method == 'POST':
        try:
            Review = request.POST['Review']
        except MultiValueDictKeyError:
            Review = False
        try:
            rating = request.POST['rating']
        except MultiValueDictKeyError:
            rating = False
        user_review = Show.objects.raw('''
            SELECT * FROM show_review
            WHERE reviewer_id=%s AND show_id=%s;
        ''',[request.user.id,id])
        if not user_review:
            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO show_review (rating,Review,reviewer_id,show_id,date_reviewed,edited)
                    VALUES(%s,%s,%s,%s,CURRENT_TIMESTAMP,False);
                ''',[rating,Review,request.user.id,id,])
        elif Review != False and rating != False and (user_review[0].Review != Review  or user_review[0].rating != int(rating)):
            print()
            print()
            print(type(user_review[0].rating))
            print(type(rating))
            print(user_review[0].rating is not int(rating))
            print()
            print()


            with connection.cursor() as cursor:
                cursor.execute('''
                    UPDATE show_review
                    SET rating=%s,Review=%s,edited=True
                    WHERE reviewer_id=%s AND show_id=%s;
                ''',[rating,Review,request.user.id,id])
        else:
            print("hello")
    movies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id=%s
        ;
    ''',[id,])
    suggested_movies = Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
        WHERE id in (SELECT show_id FROM show_show_GENRE WHERE genre_id in (SELECT id FROM show_GENRE WHERE genres in
        (SELECT genres   FROM show_GENRE WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s))
        ));
    ''',[id])
    form = search_bar()

    user_rated = True
    user_review = Show.objects.raw('''
        SELECT * FROM show_review
        WHERE reviewer_id=%s AND show_id=%s;
    ''',[request.user.id,id])
    if not len(user_review):
        user_rated = False

    castActed = Show.objects.raw('''
        SELECT * FROM cast_actors
        WHERE id in (SELECT actors_id FROM show_show_cast WHERE show_id=%s);
        ;
    ''',[id])
    langs = Show.objects.raw('''
        SELECT * FROM show_language
        WHERE id in (SELECT language_id FROM show_show_language WHERE show_id=%s);
        ;
    ''',[id])
    genres = Show.objects.raw('''
        SELECT * FROM show_GENRE
        WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s);
        ;
    ''',[id])
    directors = cast.objects.raw('''
        SELECT * FROM cast_directors
        WHERE id in (SELECT directors_id FROM show_show_director WHERE show_id=%s);
    ''',[id])
    reviews = Show.objects.raw('''
        SELECT *,username FROM show_review,auth_user
        WHERE show_review.show_id = %s AND show_review.reviewer_id = auth_user.id
        ORDER BY date_reviewed;
    ''',[id])

    avgRating =Show.objects.raw('''
        SELECT id,AVG(rating) AS KYSavg,COUNT(*) AS total FROM show_review
        WHERE show_id = %s;
    ''',[id])
    currentUser_review = Show.objects.raw('''
        SELECT *,username FROM show_review,auth_user
        WHERE show_review.show_id = %s AND show_review.reviewer_id = auth_user.id AND show_review.reviewer_id=%s;
    ''',[id,request.user.id])
    KYS_suggested_movies = Show.objects.raw('''
        SELECT id,show_id,AVG(rating) AS KYSavg FROM show_review GROUP BY show_id ORDER BY KYSavg DESC;
    ''')
    KYS_suggest = []
    all_movies =  Show.objects.raw('''
        SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show;
    ''')
    for i in KYS_suggested_movies:
        for j in all_movies:
            print(i.show_id,j.id)
            if i.show_id == j.id:
                KYS_suggest.append(j)
                break
    print(KYS_suggest)
    for i in KYS_suggest:
        print(i.titleName)
    suggested_movies = get_suggested_movies(id)
    # suggested_movies = Show.objects.raw('''
    #     SELECT *,EXTRACT(YEAR FROM releaseDate) AS year FROM show_show
    #     WHERE id in (SELECT show_id FROM show_show_GENRE WHERE genre_id in (SELECT id FROM show_GENRE WHERE genres in
    #     (SELECT genres   FROM show_GENRE WHERE id in (SELECT  genre_id FROM show_show_GENRE WHERE show_id=%s))
    #     ))
    #     ORDER BY suggested_count DESC;
    # ''',[id])
    if not currentUser_review:
        context = {
            'show':movies[0],
            'search_form':form,
            'cast':castActed,
            'Genres' : genres,
            'Languages':langs,
            'reviews':reviews,
            'Directors':directors,
            'user_rated':user_rated,
            'KYS_suggested_movies':KYS_suggested_movies,
            'RATING_INFO': False,
            'suggested_movies':suggested_movies,
        }
    else:
        total_rating = round(avgRating[0].KYSavg,2)
        context = {
            'show':movies[0],
            'search_form':form,
            'cast':castActed,
            'Genres' : genres,
            'Languages':langs,
            'reviews':reviews,
            'Directors':directors,
            'user_rated':user_rated,
            'currentUser_review':currentUser_review[0],
            'total_reviews':avgRating[0].total,
            'RATING_INFO': True,
            'KYSrating': total_rating,
            'KYS_suggested_movies':KYS_suggested_movies,
            'user_review':currentUser_review[0],
            'suggested_movies':suggested_movies,
        }
    return render(request,'show/movie.html',context)




def language_form(request):
    if request.method == 'POST':
        lform = languageForm(request.POST)
        if lform.is_valid():
            lang = lform.cleaned_data['languages']
            print("\n\n",lang,"\n\n")
            with connection.cursor() as cursor:
                cursor.execute('''
                INSERT INTO show_language (languages)
                VALUES(%s);
        ''',[lang,])
    lform = languageForm()
    all_languages = language.objects.raw('''
        SELECT * FROM show_language;
    ''')
    return render(request,'show/language_form.html',{'lform':lform,'all_languages':all_languages})


def genre_form(request):
    if request.method == "POST":
        gform = genreForm(request.POST)
        if gform.is_valid():
            genre = gform.cleaned_data['genres']
            with connection.cursor() as cursor:
                cursor.execute('''
                INSERT INTO show_genre (genres)
                VALUES(%s);
        ''',[genre,])
    gform = genreForm()
    return render(request,'show/genre_form.html',{'gform':gform})

def update_show(request,movieID):
    if request.method == "POST":
        suform = show_update_form(request.POST)
        if suform.is_valid():
            tn = suform.cleaned_data['titleName']
            rd = suform.cleaned_data['releaseDate']
            sl = suform.cleaned_data['storyLine']
            bd = suform.cleaned_data['budget']
            boc = suform.cleaned_data['BoxOfficeCollection']
            with connection.cursor() as cursor:
                cursor.execute('''
                    UPDATE show_show
                    SET titleName=%s,releaseDate=%s,storyLine=%s,budget=%s,BoxOfficeCollection=%s
                    WHERE id=%s;
                ''',[tn,rd,sl,bd,boc,movieID])
    suform = show_update_form()
    return render(request,'show/update_show.html',{'show_update_form':suform})

def user_review(request):
    user_reviews = Show.objects.raw('''
        SELECT *,show_id as MovieID FROM show_show as S,show_review as R
        WHERE R.show_id=S.id
        AND R.reviewer_id=%s;
    ''',[request.user.id])
    context = {
        'user_reviews':user_reviews,
    }
    return render(request,'show/reviews.html',context)
