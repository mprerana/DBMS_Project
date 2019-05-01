from django.shortcuts import render
from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from adverisements.forms import advform
from django.db import connection
from .models import adv
import os.path
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


def makeadv(request):
    if request.method == 'POST':
        form = advform(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.save(commit=False)
            formInstance.user = request.user
            adv_id=request.POST.get('adv_id')
            formInstance.save()
            return redirect('advertisements:viewadv',adv_id=adv_id)
    else:
        form = advform()
    return render(request, 'advertisements/create_adv.html', {
        'form': form
    })



def viewadv(request,adv_id):
    adv_id=adv_id

    a=adv.objects.get(adv_id=adv_id)

    dict = {
        't': a,
    }

    return render(request,'advertisements/viewadv.html',context=dict)
def listadv(request):

    a = adv.objects.all().order_by('-deal')

    '''n=len(a)
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if a[j].deal > a[j + 1].deal:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp'''

    dict = {
        't': a,
    }
    return render(request,'advertisements/listsadv.html', context=dict)







