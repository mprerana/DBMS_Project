import requests
from threading import Thread
from movie_booking.settings import theatre_api_key_value
import json,time,datetime,base64
from operator import itemgetter
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
from movie_booking.settings import theatre_api_key_value,MEDIA_URL
from django.template import loader




def update_tables():
    while True:
        if (time.mktime(datetime.datetime.now().timetuple())-time.mktime(update_on_database.objects.all().order_by('-last_update')[0].last_update.timetuple())) > 86400 :
            print('checking for updates')
            updated = False
            url = 'http://127.0.0.1:8000/api/'
            try:
                movie_changes = requests.get(url + 'movie_changes',
                                             headers={'Authorization': 'Token '+theatre_api_key_value})
                theatre_changes = requests.get(url + 'theatre_changes',
                                               headers={'Authorization': 'Token '+theatre_api_key_value})
                screen_changes = requests.get(url + 'screen_changes',
                                              headers={'Authorization': 'Token '+theatre_api_key_value})
                ticket_changes = requests.get(url + 'ticket_changes',
                                          headers={'Authorization': 'Token '+theatre_api_key_value})
                movie_req = requests.get(url + 'movie',
                                         headers={'Authorization': 'Token '+theatre_api_key_value})
                theatre_req = requests.get(url + 'theatre',
                                           headers={'Authorization': 'Token '+theatre_api_key_value})
                screen_req = requests.get(url + 'screen',
                                          headers={'Authorization': 'Token '+theatre_api_key_value})
                ticket_req = requests.get(url + 'ticket',
                                          headers={'Authorization': 'Token '+theatre_api_key_value})

            except:
                movie_changes = None
                theatre_changes = None
                screen_changes = None
                ticket_changes = None
                movie_req = None
                theatre_req= None
                screen_req= None
                ticket_req= None

            if movie_changes is not None and theatre_changes is not None and screen_changes is not None and ticket_changes is not None and movie_req is not None and theatre_req is not None and screen_req is not None and ticket_req is not None:
                if movie_changes.ok==True and theatre_changes.ok==True and screen_changes.ok==True and ticket_changes.ok==True and movie_req.ok==True and theatre_req.ok==True and screen_req.ok==True and ticket_req.ok==True :
                    movie_changes = sorted(json.loads(movie_changes.text), key=itemgetter('last_change'),reverse = True)
                    updated_movies=[]
                    for each in movie_changes:
                       date_time= datetime.datetime.strptime(each['last_change'], "%Y-%m-%dT%H:%M:%SZ")
                       if time.mktime(date_time.timetuple()) > time.mktime(update_on_database.objects.all().order_by('-last_update')[0].last_update.timetuple()):
                            updated_movies.append(each)
                    theatre_changes = sorted(json.loads(theatre_changes.text), key=itemgetter('last_change'), reverse=True)
                    updated_theatres = []
                    for each in theatre_changes:
                        date_time = datetime.datetime.strptime(each['last_change'], "%Y-%m-%dT%H:%M:%SZ")
                        if time.mktime(date_time.timetuple()) > time.mktime(update_on_database.objects.all().order_by('-last_update')[0].last_update.timetuple()):
                            updated_theatres.append(each)
                    screen_changes = sorted(json.loads(screen_changes.text), key=itemgetter('last_change'), reverse=True)
                    updated_screens = []
                    for each in screen_changes:
                        date_time = datetime.datetime.strptime(each['last_change'], "%Y-%m-%dT%H:%M:%SZ")
                        if time.mktime(date_time.timetuple()) > time.mktime(update_on_database.objects.all().order_by('-last_update')[0].last_update.timetuple()):
                            updated_screens.append(each)
                    ticket_changes = sorted(json.loads(ticket_changes.text), key=itemgetter('last_change'), reverse=True)
                    updated_tickets = []
                    for each in ticket_changes:
                        date_time = datetime.datetime.strptime(each['last_change'], "%Y-%m-%dT%H:%M:%SZ")
                        if time.mktime(date_time.timetuple()) > time.mktime(update_on_database.objects.all().order_by('-last_update')[0].last_update.timetuple()):
                            updated_tickets.append(each)

                    if updated_movies != []:
                        movie_req = json.loads(movie_req.text)


                        for i in range(len(updated_movies)):
                            
                            for j in range(len(movie_req)):
                                if (int(updated_movies[i]['movie_id'])==movie_req[j]['id']):
                                    break

                            d=movie_req[j]
                            movie_post_1 = base64.b64decode(d['movie_poster_1'])
                            movie_post_2 = base64.b64decode(d['movie_poster_2'])
                            movie_name = d['movie_name'].replace(" ", "")
                            filename1 = 'movies_and_cinemas/media/poster_1/' + movie_name + 'movie_poster_1.jpg'  # I assume you have a way of picking unique filenames
                            with open(filename1, 'wb') as f:
                                f.write(movie_post_1)
                            filename2 = 'movies_and_cinemas/media/poster_2/' + movie_name + 'movie_poster_2.jpg'  # I assume you have a way of picking unique filenames
                            filename2.replace(" ", "")
                            with open(filename2, 'wb') as f:
                                f.write(movie_post_2)

                            m = movie(movie_api_id=d['id'],movie_name=d['movie_name'], movie_genre=d['movie_genre'],
                                      movie_release_date=d['movie_release_date'],
                                      movie_age_rating=d['movie_age_rating'],
                                      movie_duration_mins=d['movie_duration_mins'], movie_language=d['movie_language'],
                                      movie_actors=d['movie_actors'],
                                      movie_directors=d['movie_directors'], movie_producers=d['movie_producers'],
                                      movie_writers=d['movie_writers'], imdb_movie_rating=d['imdb_movie_rating'],
                                      movie_description=d['movie_description'],
                                      movie_trailer_link=d['movie_trailer_link'],
                                      movie_poster_1='poster_1/' + movie_name + 'movie_poster_1.jpg',
                                      movie_poster_2='poster_2/' + movie_name + 'movie_poster_2.jpg')

                            m.save()

                    if updated_theatres != []:
                        theatre_req = json.loads(theatre_req.text)
                        for i in range(len(updated_theatres)):
                            for j in range(len(theatre_req)):
                                if (int(updated_theatres[i]['theatre_id'])==theatre_req[j]['id']):
                                    break
                            d=theatre_req[j]
                            if (updated_theatres[i]['change_type']=='inserted' or updated_theatres[i]['change_type']=='updated'):
                                theatre.objects.update_or_create(theatre_api_id=d['id'],defaults={'theatre_name':d['theatre_name'], 'adressline1':d['adressline1'],
                                            'adressline2':d['adressline2'], 'city':d['city'], 'state':d['state'],
                                            'pincode':d['pincode'],
                                                'theatre_rating':d['theatre_rating'],'no_of_screens':d['no_of_screens']})


                            else:
                                theatre.objects.filter(theatre_api_id=movie_req['id'])[0].delete()
                    
                    if updated_screens != []:
                        screen_req = json.loads(screen_req.text)
                        for i in range(len(updated_screens)):
                            for j in range(len(screen_req)):
                                if (int(updated_screens[i]['screen_id']) == screen_req[j]['id']):
                                    break
                            d = screen_req[j]
                            if (updated_screens[i]['change_type'] == 'inserted' or updated_screens[i][
                                'change_type'] == 'updated'):
                                screen.objects.update_or_create(screen_api_id=d['id'],
                                                                     defaults={'screen_no':d['screen_no'], 'seat_string':d['seat_string'],'theatre_id':theatre.objects.filter(theatre_api_id=d['theatre_id'])[0]})

                            else:
                                theatre.objects.filter(theatre_api_id=movie_req['id'])[0].delete()
                    
                    if updated_tickets != []:
                        ticket_req=json.loads(ticket_req.text)
                        for i in range(len(updated_tickets)):
                            for j in range(len(ticket_req)):
                                if (int(updated_tickets[i]['ticket_price_and_time_id']) == ticket_req[j]['id']):
                                    break
                            d=ticket_req[j]
                            tic = ticket_price_and_time(ticket_api_id=d['id'],movie_id=movie.objects.filter(movie_api_id=int(d['movie_id']['id']))[0],screen_id=screen.objects.filter(screen_api_id=int(d['screen_id']['id']))[0], show_timings=d['show_timings'],
                                                        date=d['date'],language=d['language'],screen_type=d['screen_type'], seat_class=d['seat_class'],
                                                        price=d['price'])
                            tic.save()

                    updated = True
                    print('updated')
                
                else:
                    print('not updated due to data not found')
            else:
                print('not updated due to server not found')
            naive = update_on_database.objects.all().order_by('-last_update')[0].last_update.replace(tzinfo=None)
            time_difference = datetime.datetime.now() - naive
            if (divmod(time_difference.total_seconds(), 60)[0] > 1440):
                time.sleep(86400)
            else:
                time.sleep(3600)
        else:
            print('sever must have restarted')
            time.sleep(87000-(time.mktime(datetime.datetime.now().timetuple())-time.mktime(update_on_database.objects.all().order_by('-last_update')[0].last_update.timetuple())))



thread=Thread(target=update_tables)
thread.start()
"""

def delete_expired_ticket():
    while True:
        print('checking if any tickets expired.')
        from django.db import connection
        cursor = connection.cursor()
        view = """
                #SELECT * FROM ticket_expire_view
"""
        cursor.execute(view)
        raw_data = cursor.fetchall()
        expired_ticket_table = []
        for each in raw_data:
            date_time=datetime.datetime.strptime(each[1],'%Y-%m-%d %H:%M:%S.%f')
            expired_ticket_table.append({'id':each[0],'time':time.mktime(date_time.timetuple())})
        expired_ticket_table=sorted(expired_ticket_table, key=lambda d: d['time'], reverse=False)
        for each in expired_ticket_table:
            if each['time'] < time.mktime(datetime.datetime.now().timetuple()):
                ticket_price_and_time.objects.get(id=each['id']).delete()
            else:
                break
        print('expired tickets are deleted.')
        time.sleep(expired_ticket_table[0]['time']+1.0-time.mktime(datetime.datetime.now().timetuple()))


thread1=Thread(target=delete_expired_ticket)
thread1.start()

"""
#__________________________________________________________________________________________________________________________

def movie_page(request, city, movie_name):
    # movie_name='Luka Chuppi'
    # city='Visakhapatnam'

    # --------------------------------------------------------------------------

    with connection.cursor() as cursor:
        Query = "SELECT t.theatre_name,CONCAT(t.adressline1, ', ', t.adressline2, ', ', t.city, ', ', t.state, ', ', t.pincode) as theatre_address,s.screen_no,tic.date,tic.show_timings   FROM  movies_and_cinemas_ticket_price_and_time as tic  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id WHERE t.city=%s AND m.movie_name=%s"
        params = [city, movie_name]
        cursor.execute(Query, params)

    row = cursor.fetchall()
    print(row)
    print('\n')
    theatre_details = []
    for i in range(len(row)):
        theatre_details.append(
            {'theatre_name': row[i][0], 'address': row[i][1], 'date': row[i][3], 'show_timings': row[i][4]})

        # --------------------------------------------------------------------------

    with connection.cursor() as cursor:
        Query = "SELECT DISTINCT t.theatre_name,CONCAT(t.adressline1, ', ', t.adressline2, ', ', t.city, ', ', t.state, ', ', t.pincode) as theatre_address,s.screen_no,tic.date  FROM  movies_and_cinemas_ticket_price_and_time as tic  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id WHERE t.city=%s AND m.movie_name=%s"
        params = [city, movie_name]
        cursor.execute(Query, params)

    row = cursor.fetchall()
    print(row)
    print('\n')
    theatre_dates = []
    for i in range(len(row)):
        theatre_dates.append({'theatre_name': row[i][0], 'address': row[i][1], 'date': row[i][3]})

        # --------------------------------------------------------------------------

    with connection.cursor() as cursor:
        Query = "SELECT  DISTINCT t.theatre_name,CONCAT(t.adressline1, ', ', t.adressline2, ', ', t.city, ', ', t.state, ', ', t.pincode) as theatre_address FROM  movies_and_cinemas_ticket_price_and_time as tic  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id WHERE t.city=%s AND m.movie_name=%s"
        params = [city, movie_name]
        cursor.execute(Query, params)

    row = cursor.fetchall()
    print(row)
    print('\n')
    theatre_address = []
    for i in range(len(row)):
        theatre_address.append({'theatre_name': row[i][0], 'address': row[i][1]})

        # --------------------------------------------------------------------------

    with connection.cursor() as cursor:
        Query = "SELECT DISTINCT m.id as movie_id,m.movie_name,m.movie_age_rating,m.movie_genre,m.movie_language,m.movie_duration_mins,m.movie_poster_1 FROM  movies_and_cinemas_ticket_price_and_time as tic  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id WHERE t.city=%s AND m.movie_name=%s"
        params = [city, movie_name]
        cursor.execute(Query, params)

    row = cursor.fetchall()
    print(row)

    movie_details = []
    for i in range(len(row)):
        movie_details.append({'movie_name': row[i][1], 'movie_age_rating': row[i][2], 'movie_genre': row[i][3],
                              'movie_language': row[i][4], 'movie_duration_mins': row[i][5],
                              'movie_poster_1': row[i][6]})

    context = {'city': city, 'movie_details': movie_details, 'theatre_address': theatre_address,
               'theatre_dates': theatre_dates, 'theatre_details': theatre_details, 'media_url': MEDIA_URL}
    # print(context)
    return render(request, "movies_and_cinemas/movie-select-show.html", context)


def city(request):
    x=theatre.objects.all().values('city').distinct()
    cities_l=[];
    for i in range(len(x)):
        cities_l.append(x[i]['city'])
    print(cities_l)
    context={'cities':cities_l}
    return render(request,"movies_and_cinemas/city.html",context)
#--------------------------------------------------------------------------------------------------------------
def show_view(request):
       with connection.cursor() as cursor:
        cursor.execute("SELECT  m.id as movie_id,m.movie_name,t.theatre_name,CONCAT(t.adressline1, ', ', t.adressline2, ', ', t.city, ', ', t.state, ', ', t.pincode) as theatre_address,s.screen_no,tic.date,tic.show_timings   FROM  movies_and_cinemas_ticket_price_and_time as tic  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id ")
       row = cursor.fetchall()
       print (row)
       print(row[0][1])
       context={'row':row}
       return render(request,"movies_and_cinemas/nxt.html",context)
#------------------------------------------------------------------------------------------------------------------
def movies_in_city_page(request,city):
       with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT  m.id as movie_id,m.movie_name,m.movie_age_rating,m.movie_genre,m.movie_language,m.movie_duration_mins,m.movie_poster_1,t.city FROM  movies_and_cinemas_ticket_price_and_time as tic  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id WHERE t.city=%s",[city])
       row = cursor.fetchall()
       print (row)
       print(row[0][1])

       movie_details=[]
       for i in range(len(row)):
         movie_details.append({'movie_name':row[i][1],'movie_age_rating':row[i][2],'movie_genre':row[i][3],'movie_language':row[i][4],'movie_duration_mins':row[i][5],'movie_poster_1':row[i][6]})
       context={'city':city,'movie_details':movie_details,'media_url':MEDIA_URL}
       print(context)
   # return HttpResponse('hello')

    #   context={'row':row}
       return render(request,"movies_and_cinemas/city_movies.html",context)


#_________________________________________________________________________________________________________________________


from collections import OrderedDict


def book_movie(request,city,ticket_id):
    context={}
    screen_=ticket_price_and_time.objects.get(id=ticket_id).screen_id
    class_of_tickets = ticket_price_and_time.objects.get(id=ticket_id).seat_class
    try:
        class_of_tickets=class_of_tickets.split(',')
    except:
        pass
    prices_of_seats = ticket_price_and_time.objects.get(id=ticket_id).price
    try:
        prices_of_seats=prices_of_seats.split(',')
    except:
        pass
    class_and_price=[]
    for i in range(len(class_of_tickets)):
        class_and_price.append({'class':class_of_tickets[i],'price':prices_of_seats[i]})
    print(class_of_tickets,prices_of_seats,class_and_price)
    context['class_and_price']=class_and_price

    url = 'http://127.0.0.1:8000/api/bookedticket'
    r = requests.get(url, headers={'Authorization': 'Token 51f39e2ea9001c26cdf14ac514c6acbba7d38f67'})
    r = json.loads(r.text)
    m=[]
    for d in r:
        n={}
        for key, value in d.items():
            n[key]=value

        m.append(n)
    seats_booked_string=''
    for i in m:
        if (i['movie_details']['id'] == int(ticket_price_and_time.objects.get(id=ticket_id).ticket_api_id)):
            seats_booked_string+=i['ticket_seat_no']


    seat_string=screen_.seat_string

    seats_booked=seats_booked_string.split(',')
    try:
        seats_booked.remove('')
    except:
        pass
    seats=seat_string.split(',')
    try:
        seats.remove('')
    except:
        pass

    for i in range(len(seats_booked)):
        seats_booked[i] = seats_booked[i].split('_')
    for i in range(len(seats)):
        seats[i] = seats[i].split('_')

    seats_booked_dict=OrderedDict()
    seats_dict=OrderedDict()

    for seat in seats_booked:
        try:
            seats_booked_dict[seat[0]].append([seat[1],seat[2]])
        except:
            seats_booked_dict[seat[0]]=[[seat[1],seat[2]],]

    for seat in seats:
        try:
            seats_dict[seat[0]].append([seat[1],seat[2]])
        except:
            seats_dict[seat[0]]=[[seat[1],seat[2]],]

    seats_booked = OrderedDict()
    seats = OrderedDict()
    for section,seat in seats_booked_dict.items():
        seats_booked[section]={}
        for each_seat in seat:
            try:
                seats_booked[section][each_seat[0]].append(each_seat[1])
            except:
                seats_booked[section][each_seat[0]]=[each_seat[1],]

    for section,seat in seats_dict.items():
        seats[section]={}
        for each_seat in seat:
            try:
                seats[section][each_seat[0]].append(each_seat[1])
            except:
                seats[section][each_seat[0]]=[each_seat[1],]

    context['seats_booked']=seats_booked
    context['seats']=seats
    context['ticket_id']=ticket_id
    context['city']=city
    return render(request,'seat_layout.html',context)


def payment(request,city):
   # user='Jagan'
   # ticket_id='qaws123'
   # selected_seats='A_9_1-A_9_2-A_9_3'
   # date_and_time=timezone.now()
   # price=450

    txn=transaction()
    txn.user=request.user
    txn.ticket_id='3456'
    txn.selected_seats='234567'
    txn.date_and_time=timezone.now()
    txn.price=210
    txn.save()

    context={'username':request.user}

    return render(request,'1.html',context)