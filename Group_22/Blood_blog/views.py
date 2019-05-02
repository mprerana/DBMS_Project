from django.shortcuts import render
from .models import Donate_blood,Comments
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def Home(request):
    return render(request,'Blood_blog/home.html')

def Blog(request):
    blogs = Donate_blood.objects.raw('''select id,Patient_name,phone_number,blood,Amount_blood,date from Blood_blog_donate_blood''')


    dicts = {
        'blogs' : blogs,
    }
    return render(request,'Blood_blog/blog.html',dicts)

def Blog2(request):
    blogs = Donate_blood.objects.raw('''select id,Patient_name,phone_number,blood,Amount_blood,date from Blood_blog_donate_blood''')
    blogs1= Donate_blood.objects.raw('''select id,Patient_name,phone_number,blood,Amount_blood,date from Blood_blog_donate_blood order by date limit 3''')
    dicts = {
        'blogs' : blogs,
        'blogs1' : blogs1
    }
    return render(request,'Blood_blog/index.html',dicts)

@login_required
def detail(request,pk):
    if pk:
        if request.method == "POST":
            user = request.user
            comment = request.POST['comment']
            cmnt = Comments(user_comment = user,comment = comment, blog_id = pk)
            cmnt.save()
        blog = Donate_blood.objects.raw('''select * from Blood_blog_donate_blood where id = {0}'''.format(pk))
        for b in blog:
            print(b)
        comments = Comments.objects.raw('''select * from Blood_blog_comments where blog_id = {0}'''.format(pk))
        return render(request,'Blood_blog/Detail.html',{'blogs' :blog ,'cmnts':comments})


@login_required
def DonationFormView(request):

    user = request.user
    if request.method == "POST":
        p_name = request.POST.get('name')
        reason = request.POST.get('reason')
        state = request.POST.get('state')
        blood = request.POST.get('blood')
        date = request.POST.get('date')
        phone = request.POST.get('phone')
        Amnt = request.POST.get('Amount')
        gender = request.POST.get('gender')
        img = request.POST.get('pic')
        form1 = Donate_blood(user=user,Patient_name=p_name,blood=blood,phone_number=phone,gender=gender,state=state,Amount_blood=Amnt,reason=reason,date=date,img=img)
        form1.save()
        return render(request,'Blood_blog/thank_you.html')
    else:
        return render(request,'Blood_blog/Request_form.html')
    return render(request,'Blood_blog/Request_form.html')

def thankyou(request):
    return render(request,'Blood_blog/thank_you.html')
