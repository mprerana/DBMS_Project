from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from customer.models import request as req
from customer.forms import request_form
from forum.models import forumdetails
from datetime import datetime

@login_required
def home(request):
    form = request_form()
    x = forumdetails.objects.all().order_by('by_date')
    print(x)
    if request.method == 'POST':
        form = request_form(request.POST)
        if form.is_valid():
            temp = req(username=request.user, request_header=form.cleaned_data['request_header'], description=form.cleaned_data['description'], amount=form.cleaned_data['amount'], by_date=form.cleaned_data['by_date'], pic=form.cleaned_data['pic'], request_date=datetime.now())
            temp.save()
            return HttpResponse("Request sent sucessfully!")
        else:
            return render(request, 'customer/home.html',{'form':form,}, {'err':form.errors,})
    return render(request, 'customer/home.html', {'form':form, 'x':x,})
