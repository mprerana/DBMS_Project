from django.shortcuts import render
from funds.forms import fund_form
from funds.models import funds, Images, comment, updates
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def home(request, pk):
    if pk:
        sub = funds.objects.get(pk=pk)
        imgs = Images.objects.filter(post=sub)
        comments = comment.objects.filter(post=sub)
        all_funds = funds.objects.all().order_by("-started_on")
        new_updates = updates.objects.all().order_by("-time")
        if request.method == 'POST':
            if request.POST.get('update') == 'Update':
                new_up = updates(post=sub, update=request.POST['new'], time=datetime.now())
                new_up.save()
                url = reverse('funds:home_with_pk', kwargs={'pk': sub.pk})
                return HttpResponseRedirect(url)
            elif request.POST.get('update') == 'Submit':
                new_com = comment(post=sub, message=request.POST['msg'], user=request.user)
                new_com.save()
                url = reverse('funds:home_with_pk', kwargs={'pk': sub.pk})
                return HttpResponseRedirect(url)
        return render(request, 'reliffunds/base.html', {'updates':new_updates,'sub':sub, 'imgs':imgs, 'comments':comments, 'funds':all_funds})
    else:
        return HttpResponseRedirect(reverse('admin_login:home'));
