from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    context = {
        "data": "this is home page"
    }
    return render(request, 'registration/home.html', context=context)



