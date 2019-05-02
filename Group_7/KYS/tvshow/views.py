from django.shortcuts import render
from django.http import HttpResponse
from tvshow.models import TVShow
from show.models import Show
from .forms import seriesForm, seasonForm, episodeForm
from django.db import connection


# Create your views here.

def tvshowpage(request, id):
    tvshow = TVShow.objects.raw('''
            SELECT * FROM tvshow_tvshow
            WHERE id = %s;
    ''', [id])
    genres = Show.objects.raw('''
            SELECT * FROM show_genre
            WHERE id in (SELECT genre_id FROM tvshow_tvshow_genre WHERE tvshow_id=%s);
            ;
        ''', [id])
    language = Show.objects.raw('''
            SELECT * FROM show_language
            WHERE id in (SELECT language_id FROM tvshow_tvshow_language WHERE tvshow_id=%s);
            ;
        ''', [id])
    seasons = TVShow.objects.raw('''
            SELECT * FROM tvshow_season
            WHERE id in (SELECT season_id FROM tvshow_episode WHERE series_id=%s);
            ;
        ''', [id])
    cast = TVShow.objects.raw('''
            SELECT * FROM cast_cast WHERE id in (SELECT cast_id FROM tvshow_episode_cast WHERE episode_id
            in (SELECT episode_id FROM tvshow_episode WHERE series_id=%s));
            ;
    ''', [id])
    context = {'tvshow': tvshow[0], 'genres': genres, 'langs': language, 'seasons': seasons, 'cast': cast }

    with connection.cursor() as cursor:
        cursor.execute('''
            CALL update_series_count(@%s);
        ''',[id])
    with connection.cursor() as cursor:
        cursor.execute('''
            UPDATE tvshow_tvshow
            SET seriesViewCount = seriesViewCount + 1
            WHERE id = %s;
        ''',[id])
    return render(request, 'tvshow/tvshow_page.html', context)


def seasonpage(request, series_id, season_id):
    episodes = TVShow.objects.raw('''
            SELECT * FROM tvshow_episode
            WHERE series_id=%s AND season_id=%s;
    ''', [series_id, season_id])
    for i in episodes:
        print(i.episodePoster)
    tvshow = TVShow.objects.raw('''
            SELECT * FROM tvshow_tvshow
            WHERE id =%s;
    ''', [series_id,])
    context = {'episodes' : episodes, 'tvshow' : tvshow[0], 'season_id' : season_id,}
    return render(request, 'tvshow/season_page.html', context)


def episodepage(request, series_id, season_id, episodeNum):
    series = TVShow.objects.raw('''
                SELECT * FROM tvshow_tvshow
                WHERE id = %s
                ;
        ''', [series_id, ])
    season = TVShow.objects.raw('''
                SELECT * FROM tvshow_season
                WHERE id = %s
                ;
        ''', [season_id, ])

    episode = TVShow.objects.raw('''
            SELECT * FROM tvshow_episode
            WHERE id in (SELECT id FROM tvshow_episode WHERE series_id=%s AND season_id = %s AND episodeNum = %s )
            ;
    ''', [series_id, season_id, episodeNum])

    cast = Show.objects.raw('''
            SELECT * FROM cast_cast
            WHERE id in (SELECT cast_id FROM tvshow_episode_cast WHERE episode_id in
                                                                    (SELECT id FROM tvshow_episode WHERE episodeNum=%s)
            )

    ''', [episodeNum])
    context = {'episode' : episode[0], 'series' : series[0], 'season': season[0],'cast':cast}
    return render(request, 'tvshow/episode_page.html', context)
