from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from userlogin.models import Profile
from verifier.models import  pending_request
from customer.models import request as req
from forum.models import forumdetails
from funds.forms import fund_form, imgform
from funds.models import funds, Images
from datetime import datetime
from django.forms import modelformset_factory
from django.contrib import messages
from funds.models import funds
from User.models import Event

@login_required
def req_appoint(request, pk):
    temp = req.objects.get(pk=pk)
    new_pr = pending_request(appointed_by = request.user.username, username = temp.username, request_header = temp.request_header, description = temp.description, amount = temp.amount, by_date = temp.by_date, pic = temp.pic, request_date = temp.request_date)
    new_pr.save()
    temp.delete()
    return HttpResponseRedirect(reverse('admin_login:home'))

@login_required
def req_cancel(request, pk):
     temp = req.objects.get(pk=pk)
     temp.delete()
     return HttpResponseRedirect(reverse('admin_login:home'))

@login_required
def req2_verify(request, pk):
     temp = pending_request.objects.get(pk=pk)
     new_bd = forumdetails(username = temp.username, request_header = temp.request_header, description = temp.description, amount = temp.amount, by_date = temp.by_date, pic = temp.pic)
     new_bd.save()
     temp.delete()
     return HttpResponseRedirect(reverse('admin_login:home'))

@login_required
def req2_cancel(request, pk):
     temp = pending_request.objects.get(pk=pk)
     temp.delete()
     return HttpResponseRedirect(reverse('admin_login:home'))


@login_required
def home(request):
    form = fund_form()
    ImageFormSet = modelformset_factory(Images,form=imgform, min_num=5, max_num=5,extra=5)
    formset = ImageFormSet(queryset=Images.objects.none())
    if request.method == 'POST':
        form = fund_form(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid():
            usr = request.user
            new_fund = funds(by=usr, started_on=datetime.now(), title=form.cleaned_data['title'], report=form.cleaned_data['report'], place=form.cleaned_data['place'],state=form.cleaned_data['state'],target=form.cleaned_data['target'],)
            new_fund.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(post=new_fund, image=image)
                    photo.save()
            messages.success(request, "Fund raised successfully!")
            return HttpResponseRedirect(reverse('admin_login:home'))
        else:
            messages.error(request, form.errors)
            if formset.errors:
                messages.error(request, 'Please upload 5 images!')
            #return render(request, 'admin/home.html', {'err':form.errors,})

    current_user = request.user
    #cuser = UserProfile.objects.raw('''select * from appname_tablename where prof=%s''',[current_user])
    cuser = Profile.objects.filter(user=current_user).values()
    print(cuser)
    #new_requests = req.objects.raw('''select * from appname_tablename''')
    new_requests = req.objects.all()
    #pend_req = pending_request.objects.raw('''select * from appname_tablename where appointed_by=%s''',[current_user.username])
    pend_req = pending_request.objects.filter(appointed_by = current_user.username)
    form = fund_form()
    ImageFormSet = modelformset_factory(Images,form=imgform, extra=5)
    formset = ImageFormSet(queryset=Images.objects.none())
    fund = funds.objects.all().order_by('started_on')
    events=Event.objects.filter(verifierassigned=current_user)
    return render(request, 'admin/home.html', {'user': current_user, 'c':cuser, 'requests':new_requests, 'request2':pend_req, 'form':form, 'formset':formset, 'funds':fund,'events':events})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic'))


@login_required
def verifyevent(request):
    eventid=request.POST["eventid"]
    Event.objects.filter(eventid=eventid).update(verified=True)
    return home(request)
