from django.shortcuts import render
from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings

from shop.forms import ShopAdd,writereview
from django.db import connection
import os.path
import os
import random
import io
import base64
from PIL import Image
from django.core.files.storage import FileSystemStorage




mycursor = connection.cursor()

print('f')

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def makeshop(request):
    sid = random.randrange(100, 500, 3)
    print('a')
    if request.method =='POST':
        print('b')
        if 'proof' in request.FILES and request.POST:
            os.remove(os.path.join(settings.MEDIA_ROOT,'shop/images/img.png'))
            image = request.FILES['proof']
            fs_img = FileSystemStorage(
                location=settings.FS_IMAGE_UPLOADS,
                base_url=settings.FS_IMAGE_URL
            )
            imageName = fs_img.save(image.name, image)

        form = ShopAdd(request.POST)

        if form.is_valid():
            print('c')
            sname = request.POST.get('sname')
            a_id = request.POST.get('a_id')
            open_time = request.POST.get('open_time')
            close_time = request.POST.get('close_time')
            expiry = request.POST.get('Registered_for')
            t_id= request.POST.get('tid')
            owner_name = request.POST.get('owner_name')
            tenant_name = request.POST.get('tenant_name')
            floor = request.POST.get('floor')
            description=request.POST.get('Description')
            category=request.POST.get('category')

            integer=int(close_time)
            if (integer>12):
                integer=integer-12

            close_time=str(integer)
            img = Image.open("media/shop/images/img.png", mode='r')
            imgByteArr = io.BytesIO()
            img.save(imgByteArr, format='PNG')
            imgByteArr = imgByteArr.getvalue()



            sql = "INSERT INTO shop (sname,a_id,open_time,close_time,expiry,t_id,owner_name,tenant_name,floor,description,sid,image,category) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(sname,a_id,open_time,close_time,expiry,t_id,owner_name,tenant_name,floor,description,sid,imgByteArr,category)

            mycursor.execute(sql,values)


            return redirect('shop:viewshop',sid=sid)
    else:
        form = ShopAdd()
        return render(request, 'shop/create_shop.html',{'form': form})



def viewshop(request,sid):
    sid=sid
    mycursor.execute("SELECT * FROM shop WHERE sid LIKE %s",[sid])
    a=mycursor.fetchall()
    mycursor.execute("SELECT * FROM reviews WHERE sid LIKE %s", [sid])
    b = mycursor.fetchall()

    file = io.BytesIO(a[0][10])
    img1 = Image.open(file)
    img1.save("shop/static/shop/images/image.png")

    dict = {
        't': a,
        'x':b,
        'y':img1,
    }

    return render(request,'shop/viewshop.html',context=dict)

def listshops(request):
    mycursor.execute("SELECT * FROM shop")
    a = mycursor.fetchall()
    print(a)
    dict = {'t': a}
    img=['shop/static/shop/images/1.png','shop/static/shop/images/2.png','shop/static/shop/images/3.png','shop/static/shop/images/4.png','shop/static/shop/images/5.png','shop/static/shop/images/6.png','shop/static/shop/images/7.png']

    return render(request,'shop/listshops.html', context=dict)

def categlistshops(request,category):
    category=category
    mycursor.execute("SELECT * FROM shop WHERE category LIKE %s",[category])
    a = mycursor.fetchall()
    print(a)
    dict = {'t': a}
    img=['shop/static/shop/images/1.png','shop/static/shop/images/2.png','shop/static/shop/images/3.png','shop/static/shop/images/4.png','shop/static/shop/images/5.png','shop/static/shop/images/6.png','shop/static/shop/images/7.png']

    return render(request,'shop/categlistshops.html', context=dict)

def category(request):
    return render(request,'shop/category.html')


def reviewtext(request,sid):
    shopid = sid
    review_id=random.randrange(200, 500, 3)
    if request.method == 'POST':
        form = writereview(request.POST)
        if form.is_valid():
            content = request.POST.get('review')
            username = request.POST.get('name')
            sql ="INSERT INTO reviews (sid,review,name,review_id) VALUES (%s,%s,%s,%s)"
            values = (shopid,content,username,review_id)

            mycursor.execute(sql, values)
            return redirect('/shop/listshops/viewshop/' + str(sid) + '/')
    else:
        form = writereview()
    return render(request, 'shop/writereview.html', {'form': form})


