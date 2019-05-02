from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection,transaction
from .flight import flight_data
from .hotel import hotel_show
from .hotel_details import room_book
import datetime

from .flight import flights
import requests

a = []
def hotel_view(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM Book_Hotels where user_id_id={}  ORDER BY booking_date DESC;".format(request.user.id))
    hotels_booked=cursor.fetchall()
    hotels_booked=list(hotels_booked)
    for i in range(len(hotels_booked)):
        hotels_booked[i]=list(hotels_booked[i])
    for i in hotels_booked:
        str1=i[7]
        lst = str1.split('$')
        l2=[]
        for j in lst:
            l2.append(j.split("+"))
        i[7]=l2

    print(hotels_booked)
    return render(request,'Book/hotels_booked.html',{'hotels':hotels_booked})

def flight_view(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM Book_Flights where user_id_id={}  ORDER BY book_date DESC;".format(request.user.id))
    flights_booked=cursor.fetchall()
    flights_booked = list(flights_booked)
    for i in range(len(flights_booked)):
        flights_booked[i] = list(flights_booked[i])
    for i in flights_booked:
        str1 = i[11]
        lst = str1.split('$')
        l2 = []
        for j in lst:
            l2.append(j.split("+"))
        i[11] = l2
    #len2 = len(flights_booked[7])

    print(flights_booked)

    return render(request,'Book/flights_booked.html',{'flights':flights_booked})
def hotel_search(request):
    if request.method=='POST':
        city=request.POST.get('city')
        state=request.POST.get('state')
        adults=request.POST.get('adults')
        check_in_date=request.POST.get('check_in_date')
        check_in_date = datetime.datetime.strptime(str(check_in_date), '%Y-%m-%d').strftime('%d-%m-20%y')
        check_out_date=request.POST.get('check_out_date')
        check_out_date = datetime.datetime.strptime(str(check_out_date), '%Y-%m-%d').strftime('%d-%m-20%y')
        All_hotels=hotel_show(city,state,check_in_date,check_out_date)

        c = 0
        names = []
        for i in range(len(All_hotels)):
            n = []
            n.append('name' + str(i + 1))
            n.append('address' + str(i + 1))
            n.append('hotel_id' + str(i + 1))
            n.append('pic' + str(i + 1))
            n.append('button' + str(i + 1))

            names.append(n)
        print(names)
        names2 = zip(All_hotels, names)
        print(names2)
        return render(request, 'Book/hotel_book.html', {'hotel1': All_hotels, 'c': c, 'names': names, 'names2': names2,'adults':adults,'check_in_date': check_in_date,'check_out_date':check_out_date})
    else:
        return render(request,'Book/hotel_search.html')
def hotel_details(request):
    value = request.POST.get('button')
    value = value.replace('button', '')
    hotel_id = request.POST.get('hotel_id{}'.format(value))
    adults=request.POST.get('adults')
    b = []
    for i in range(int(adults)):
        b.append(i + 1)
    check_in_date=request.POST.get('check_in_date')
    check_out_date=request.POST.get('check_out_date')
    hotel_details=room_book(hotel_id)
    print(hotel_details)

    return render(request,'Book/hotel_details.html',{'b':b,'hotel_details':hotel_details,'adults':adults,'check_in_date':check_in_date,'check_out_date':check_out_date})
def hotel_book(request):
    adults = request.POST.get('adults')
    print('\n\n',type(adults))
    b=[]
    for i in range(int(adults)):
        b.append(i+1)

    check_in_date = request.POST.get('check_in_date')
    check_out_date = request.POST.get('check_out_date')
    user_id = request.user.id
    hotel_name=request.POST.get('hotel_name')
    print('\n\n')
    print(hotel_name)
    address=request.POST.get('address')
    price=request.POST.get('price')
    booking_date=datetime.datetime.now()
    details = ''
    for i in b:
        f_name = request.POST.get('fname' + str(i))
        l_name = request.POST.get('lname' + str(i))
        age = request.POST.get('Age' + str(i))
        gender = request.POST.get('Gender' + str(i))

        details += f_name + '+' + l_name + '+' + str(age) + '+' + gender + '$'
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Book_Hotels(user_id_id,hotel_name,address,price,check_in_date,check_out_date,booking_date,details) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",(request.user.id,hotel_name,address,price,check_in_date,check_out_date,booking_date,price))
    transaction.commit()
    return redirect('/credits/?total_cost={}&book_date={}'.format(price,booking_date))
def flight_search(request):
    if request.method=='POST':
        origin=request.POST.get('from')
        to=request.POST.get('to')
        adults=request.POST.get('adults')
        date2=request.POST.get('date')
        date=datetime.datetime.strptime(str(date2), '%Y-%m-%d').strftime('%d-%m-20%y')
        print(date)
        date = date.replace('-','/')
        print('\n\n')
        print(origin,to,adults,date)
        flights=[]
        flights=flight_data(origin,to,date,adults)

        c=0
        names=[]
        for i in range(len(flights)):
            n=[]
            n.append('flight_name'+str(i+1))
            n.append('flight_code' + str(i+1))
            n.append('dept_city' + str(i+1))
            n.append('dept_time' + str(i+1))
            n.append('no_of_stops' + str(i+1))
            n.append('reach_time' + str(i+1))
            n.append('duration' + str(i+1))
            n.append('arrival_city' + str(i+1))
            n.append('price' + str(i+1))
            n.append('button'+str(i+1))
            names.append(n)
        #print(names)
        names2=zip(flights,names)
        return render(request,'Book/booked.html',{'flights1':flights,'c':c,'names':names,'names2':names2,'date':date2,'adults':adults})
    else:
        return render(request,'Book/flight_search.html')
def booked(request):
    value=request.POST.get('button')
    value=value.replace('button','')
    flight_name = request.POST.get('flight_name{}'.format(value))
    flight_code = request.POST.get('flight_code{}'.format(value))
    dept_city = request.POST.get('dept_city{}'.format(value))
    dept_time = request.POST.get('dept_time{}'.format(value))
    no_of_stops = request.POST.get('no_of_stops{}'.format(value))
    reach_time = request.POST.get('reach_time{}'.format(value))
    duration = request.POST.get('duration{}'.format(value))
    arrival_city = request.POST.get('arrival_city{}'.format(value))
    price = request.POST.get('price{}'.format(value))
    adults=request.POST.get('adults')
    date=request.POST.get('date')
    b = []
    for i in range(int(adults)):
        b.append(i + 1)

    a.append(flight_name)
    a.append(flight_code)
    a.append(dept_city)
    a.append(dept_time)
    a.append(no_of_stops)
    a.append(reach_time)
    a.append(duration)
    a.append(arrival_city)
    a.append(price)

    return render(request,'Book/booked1.html',{'b':b,'a':a,'date':date,'adults':adults})
def ticket_book(request):
    user_id=request.user.id
    flight_name = request.POST.get('fli_name')
    flight_code = request.POST.get('fli_code')
    dept_city = request.POST.get('dept_city')
    dept_time = request.POST.get('dept_time')
    no_of_stops = request.POST.get('no_stops')
    reach_time = request.POST.get('reach_time')
    duration = request.POST.get('duration')
    arrival_city = request.POST.get('arr_city')
    price = request.POST.get('price')
    book_date=datetime.datetime.now()
    adults=request.POST.get('adults')
    date2=request.POST.get('date')
    price = price[-5:].replace(',', '')
    total_cost = int(price)*int(adults)
    b = []
    for i in range(int(adults)):
        b.append(i + 1)
    details = ''
    for i in b:
        f_name=request.POST.get('fname'+str(i))
        l_name = request.POST.get('lname'+str(i))
        age = request.POST.get('Age'+str(i))
        gender = request.POST.get('Gender'+str(i))

        details += f_name+'+'+l_name+'+'+str(age)+'+'+gender+'$'
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Book_Flights(user_id_id,flight_name,flight_code,date,dept_city,dept_time,no_of_stops,reach_time,duration,arrival_city ,price,book_date,details) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(request.user.id,flight_name,flight_code,date2,dept_city,dept_time,no_of_stops,reach_time,duration,arrival_city,price,book_date,details))
    transaction.commit()

    return redirect('/credits/?total_cost={}&book_date={}'.format(total_cost,book_date))