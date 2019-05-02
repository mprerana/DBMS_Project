from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from .models import rate,service
from .models import rate
from django.urls import reverse
from .forms import ReviewForm,filters
import datetime
from django.db import transaction,connection
from django.db.models import Avg

hotel = None

def review_list(request):
    global hotel
    if request.method == 'POST':

        if 'positive' in request.POST:
            cursor = connection.cursor()
            cursor.callproc('reviewfilter',[1,'{}'.format(hotel)])
            latest_review_list=cursor.fetchall()

            form = ReviewForm()
            avg, one, two, three, four, five = 0, 0, 0, 0, 0, 0
            cursor.execute("SELECT AVG(rating) FROM user_reviews_rate")
            avg = cursor.fetchone()
            avg=avg[0]
            #avg=round(avg,2)
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber',[1,'{}'.format(hotel)])
            one=cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber',[2,'{}'.format(hotel)])
            two=cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber',[3,'{}'.format(hotel)])
            three=cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber',[4,'{}'.format(hotel)])
            four=cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber',[5,'{}'.format(hotel)])
            five=cursor.fetchone()[0]
            t = len(latest_review_list)
            if t == 0:
                p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
            else:
                p1, p2, p3, p4, p5 = float((one / t) * 100), float((two / t) * 100), float((three / t) * 100), float(
                    (four / t) * 100), float((five / t) * 100)

            context = {'form': form, 'latest_review_list': latest_review_list, 'avg': avg, 'one': one, 'two': two,
                       'three': three, 'four': four, 'five': five, 't': t, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4,
                       'p5': p5}
            return render(request, 'templates/user_reviews/review_list.html', context)

        if 'critical' in request.POST:
            cursor = connection.cursor()
            cursor.callproc('reviewfilter', [2,'{}'.format(hotel) ])
            latest_review_list = cursor.fetchall()
            form = ReviewForm()
            avg, one, two, three, four, five = 0, 0, 0, 0, 0, 0
            cursor.execute("SELECT AVG(rating) FROM user_reviews_rate")
            avg = cursor.fetchone()
            avg = avg[0]
            #avg = round(avg, 2)
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [1,'{}'.format(hotel) ])
            one = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [2,'{}'.format(hotel) ])
            two = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [3,'{}'.format(hotel) ])
            three = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [4,'{}'.format(hotel) ])
            four = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [5,'{}'.format(hotel) ])
            five = cursor.fetchone()[0]
            t = len(latest_review_list)
            if t == 0:
                p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
            else:
                p1, p2, p3, p4, p5 = float((one / t) * 100), float((two / t) * 100), float((three / t) * 100), float(
                    (four / t) * 100), float((five / t) * 100)
            context = {'form': form, 'latest_review_list': latest_review_list, 'avg': avg, 'one': one, 'two': two,
                       'three': three, 'four': four, 'five': five, 't': t, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4,
                       'p5': p5}
            return render(request, 'templates/user_reviews/review_list.html', context)


        if 'latest' in request.POST:
            cursor = connection.cursor()
            cursor.callproc('reviewfilter', [3, '{}'.format(hotel)])
            latest_review_list = cursor.fetchall()
            form = ReviewForm()
            avg, one, two, three, four, five = 0, 0, 0, 0, 0, 0
            cursor.execute("SELECT AVG(rating) FROM user_reviews_rate")
            avg = cursor.fetchone()
            avg = avg[0]
            #avg = round(avg, 2)
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [1,'{}'.format(hotel) ])
            one = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [2,'{}'.format(hotel) ])
            two = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [3,'{}'.format(hotel) ])
            three = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [4,'{}'.format(hotel) ])
            four = cursor.fetchone()[0]
            cursor.close()
            cursor = connection.cursor()
            cursor.callproc('ratingnumber', [5,'{}'.format(hotel) ])
            five = cursor.fetchone()[0]
            t = len(latest_review_list)
            if t == 0:
                p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
            else:
                p1, p2, p3, p4, p5 = float((one / t) * 100), float((two / t) * 100), float((three / t) * 100), float(
                    (four / t) * 100), float((five / t) * 100)
            context = {'form': form, 'latest_review_list': latest_review_list, 'avg': avg, 'one': one, 'two': two,
                       'three': three, 'four': four, 'five': five, 't': t, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4,
                       'p5': p5}
            return render(request, 'templates/user_reviews/review_list.html', context)

    else:

        hotel = request.GET.get('hotel')
        cursor = connection.cursor()
        cursor.callproc('reviewfilter', [3,'{}'.format(hotel) ])
        latest_review_list = cursor.fetchall()

        form = ReviewForm()
        avg, one, two, three, four, five = 0, 0, 0, 0, 0, 0
        cursor.execute("SELECT AVG(rating) FROM user_reviews_rate")
        avg = cursor.fetchone()
        avg = avg[0]
        #avg = round(avg, 2)
        cursor.close()
        cursor = connection.cursor()
        cursor.callproc('ratingnumber', [1,'{}'.format(hotel) ])
        one = cursor.fetchone()[0]
        cursor.close()
        cursor = connection.cursor()
        cursor.callproc('ratingnumber', [2,'{}'.format(hotel) ])
        two = cursor.fetchone()[0]
        cursor.close()
        cursor = connection.cursor()
        cursor.callproc('ratingnumber', [3, '{}'.format(hotel)])
        three = cursor.fetchone()[0]
        cursor.close()
        cursor = connection.cursor()
        cursor.callproc('ratingnumber', [4,'{}'.format(hotel) ])
        four = cursor.fetchone()[0]
        cursor.close()
        cursor = connection.cursor()
        cursor.callproc('ratingnumber', [5,'{}'.format(hotel) ])
        five = cursor.fetchone()[0]
        t = len(latest_review_list)
        if t==0:
            p1,p2,p3,p4,p5=0,0,0,0,0
        else:
            p1, p2, p3, p4, p5 = float((one / t) * 100), float((two / t) * 100), float((three / t) * 100), float(
                (four / t) * 100), float((five / t) * 100)



        context = {'form':form,'hotel':hotel,'latest_review_list':latest_review_list,'avg':avg,'one':one,'two':two,'three':three,'four':four,'five':five,'t':t,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5}
        return render(request, 'templates/user_reviews/review_list.html/', context)



def add_review(request):
    global hotel
    hotel=request.POST.get('hotel')
    hotel=hotel.replace(' ','+')
    form = ReviewForm(request.POST)
    if form.is_valid():
        #type = form.cleaned_data['service_type']
        org = hotel
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_id = request.user.username
        pdate = datetime.datetime.now()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user_reviews_rate(user,service_name,rating,comment,published_date) VALUES(%s,%s,%s,%s,%s);", (user_id,org,rating,comment,pdate))

        transaction.commit()

        return redirect('/reviews/?hotel={}'.format(hotel))
    return HttpResponse('invalid!!!')

