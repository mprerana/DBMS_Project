from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from forum.models import forumdetails, commentinfo
from django.contrib.auth.decorators import login_required

@login_required
def home(request, pk):
    if pk:
        if request.method == 'POST':
            if len(request.POST['msg']) > 1:
                c_user = request.user
                new_comment = commentinfo(message = request.POST['msg'], by = c_user )
                new_comment.to = forumdetails.objects.get(pk=pk)
                new_comment.save()
        reqs = forumdetails.objects.all()
        forum = forumdetails.objects.get(pk=pk)
        comments = commentinfo.objects.filter(to = forum.pk)
        print(forum)
        print(comments)
        return render(request, 'forum/base.html', {'reqs':reqs, 'forum':forum, 'comments':comments})
    else:
        return HttpResponseRedirect(reverse('cus_login:home'));
