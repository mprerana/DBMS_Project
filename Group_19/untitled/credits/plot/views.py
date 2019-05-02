# Create your views here.
from django.db import connection
from django.contrib.auth.models import User

from credits.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
import random

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

import random




cursor = connection.cursor()


def test(request):
    cursor.execute("SELECT * FROM shops")
    b=cursor.fetchall()
    print(b)
    return HttpResponse(b[0])
def see(request):
    user_name = request.user.username
    print(user_name)
    print('helloworld')

    user_id = User.objects.get(username=request.user.username).pk
    cursor.execute("""SELECT * FROM plot_details WHERE admin_id <>%s """ % (int(user_id)))
    b=cursor.fetchall()
    plots=''
    print(b)
    t_dict = {'t': b,'plots':'rent'}
    return render(request, 'plot/first.html', context=t_dict)
def view(request,p_id=None):
    p=p_id
    if request.method=='POST':
        mode= request.POST.get('mode')
        cost= request.POST.get('cost')
        area = request.POST.get('area')
        cursor.execute("""SELECT floor FROM plot_details WHERE p_id = %s""" % (p))

        a = cursor.fetchone()
        floor = a[0]
        t_dict={'mode':mode,'cost':cost,'area':area,'p_id':p_id,'floor':floor}
        return render(request, 'plot/show.html', context=t_dict)

@login_required(login_url='homepage:user_login')
def confirm(request,p_id=None):
    if request.method=='POST':
        mode= request.POST.get('mode')
        cost= request.POST.get('cost')
        area = request.POST.get('area')
        floor = request.POST.get('floor')
        t_dict={'mode':mode,'cost':cost,'area':area,'p_id':p_id,'floor':floor}
        return render(request, 'plot/confirm.html', context=t_dict)

@login_required(login_url='homepage:user_login')
def final(request,p_id=None):
    print('ffg')
    p=p_id
    cost = request.POST.get('cost')
    i = random.randrange(100, 1000, 3)

    if request.method=='POST':
        if 'BUY' in request.POST:
            print("hihiik")
            cursor.execute("""SELECT admin_id FROM plot_details WHERE p_id = %s""" % (p))
            a = cursor.fetchone()
            a = a[0]
            q=1
            print('grsdgrd')
            user_name = request.user.username
            print(user_name)
            user_id = User.objects.get(username=request.user.username).pk
            print('a='+str(a))
            print(p);print(a);print(cost);
            sql = "INSERT INTO sold_transactions (p_id,a_id,user_id,amount) VALUES (%s,%s,%s,%s)"
            val = (p, a,int(user_id),float(cost))
            cursor.execute(sql, val)
            print('hiiererer')
           # cursor.execute("""SELECT balance FROM plot_details WHERE p_id = %s""" % (p))

            cursor.execute("UPDATE plot_details SET admin_id = %s WHERE p_id=%s " % (user_id,p))
            print('hii')


            balance = {'bal':100}
            return render(request, 'credits/index.html', context=balance)
            '''if b[0] in l:
                query = """ UPDATE plot_details SET admin_id = %s WHERE p_id =%s"""

                data = (b[0], p)
                cursor.execute(query,data)

                cursor.execute("""SELECT admin_id FROM plot_details WHERE p_id = %s""" % (p))

                a = cursor.fetchone()
                a = a[0]
                print(a)
                sql = "INSERT INTO sold_transactions (p_id,a_id,user_id,amount) VALUES (%s,%s,%s,%s)"

                val = (p,a,b[0],float(cost))
                cursor.execute(sql, val)
                print('hiiererer')
                return HttpResponse("You bought the plot")

            else:
                sql = "INSERT INTO admin (name, age,phone_num,a_id,street,city,state) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                val = (b[1],b[2],b[5],b[0],b[6],b[7],b[8])
                cursor.execute(sql, val)
                cursor.execute("UPDATE plot_details SET admin_id=b[0] WHERE p_id=p")
                cursor.execute("""SELECT admin_id FROM plot_details WHERE p_id = %s""" % (p))

                a = cursor.fetchone()
                a = a[0]
                print(a)
                sql = "INSERT INTO sold_transactions (p_id,a_id,user_id,amount) VALUES (%s,%s,%s,%s)"

                val = (p, a, b[0], float(cost))
                cursor.execute(sql, val)

                return HttpResponse("You bought the plot")'''
        elif 'TAKE_FOR_RENT' in request.POST:
            print("hihiik")
            #cursor.execute("SELECT * FROM tenants")
            #b=cursor.fetchall()
            '''l=[]
            for i in b:
                l.append(i[4])'''

            cursor.execute("""SELECT admin_id FROM plot_details WHERE p_id = %s""" % (p))
            a = cursor.fetchone()
            a = a[0]
            user_name = request.user.username
            print(user_name)
            user_id = User.objects.get(username=request.user.username).pk
            date = datetime.date.today()
            date += datetime.timedelta(days=30)
            print(p);print(a);print(id);print(float(cost));print(date);
            sql = "INSERT INTO rent_transactions (p_id,a_id,user_id,monthly_amount,next_due_date,status) VALUES (%s,%s,%s,%s,%s,%s)"
            q='pending'
            #print(b[0])
            val = (p, a,int(user_id), float(cost), date,q)
            cursor.execute(sql, val)
            query = """ UPDATE plot_details SET tenant_id = %s WHERE p_id =%s"""
            data = (int(user_id), p)
            cursor.execute(query, data)


            print('hiiererer')

            balance = {'bal': 100}
            return render(request, 'credits/index.html', context=balance)
            '''if b[0] in l:
                query = """ UPDATE plot_details SET tenant_id = %s WHERE p_id =%s"""

                data = (b[0], p)
                cursor.execute(query,data)

                cursor.execute("""SELECT admin_id FROM plot_details WHERE p_id = %s""" % (p))

                a = cursor.fetchone()
                a=a[0]

                sql = "INSERT INTO rent_transactions (p_id,a_id,user_id,monthly_amnt,next_due_date) VALUES (%s,%s,%s,%s,%s)"

                val = (p,a,b[0],float(cost),'12-01-2020')
                cursor.execute(sql, val)
                print('hiiererer')
                return HttpResponse("You bought the plot for rent")

            else:
                sql = "INSERT INTO tenants (name, age,address,phone_num,t_id) VALUES (%s,%s,%s,%s,%s)"
                val = (b[1], b[2], b[6],b[4],b[0])
                cursor.execute(sql, val)
                query = """ UPDATE plot_details SET tenant_id = %s WHERE p_id =%s"""

                data = (b[0], p)
                cursor.execute(query, data
                cursor.execute("""SELECT admin_id FROM plot_details WHERE p_id = %s""" % (p))

                a = cursor.fetchone()
                a = a[0]

                sql = "INSERT INTO rent_transactions (p_id,a_id,user_id,monthly_amnt,next_due_date) VALUES (%s,%s,%s,%s,%s)"

                val = (p, a, b[0], float(cost), '12-01-2020')
                cursor.execute(sql, val)
                print('hiiererer')
                return HttpResponse("You bought the plot for rent")'''
def rent(request):
    user_name = request.user.username
    print(user_name)
    user_id = User.objects.get(username=request.user.username).pk
    us=int(user_id)
    cursor.execute("""SELECT * FROM plot_details WHERE (admin_id<>%s)  """ % (int(user_id)))
    b=cursor.fetchall()
    plots=''
    print(b)
    t_dict = {'t': b,'plots':'rent'}
    return render(request, 'plot/first.html', context=t_dict)
def buy(request):
    user_name = request.user.username
    print(user_name)
    user_id = User.objects.get(username=request.user.username).pk
    cursor.execute("""SELECT * FROM plot_details WHERE admin_id <>%s""" % (int(user_id)))
    b=cursor.fetchall()
    plots=''
    print(b)
    t_dict = {'t': b,'plots':'buy'}
    return render(request, 'plot/first.html', context=t_dict)
def pay_rent(request):
    balances = AccountBalance.objects.filter(user=request.user)
    print(balances)

    balance = {'bal': balances}
    return render(request, 'credits/index.html', context=balance)
def cancel(request):
    return render(request,'plot/cancel.html')




