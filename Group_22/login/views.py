from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from userlogin.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    # Create your views here.

    return render(request, "login/home.html")

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request.POST)
        uname = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        admin = authenticate(username=uname, password=password)

        if admin:
            x = Profile.objects.get(user=admin)
            if admin.is_active and x.user_type == 'V':
                login(request,admin)
                return HttpResponseRedirect(reverse('admin_login:home'))
            elif admin.is_active and x.user_type == 'C':
                login(request,admin)
                #return HttpResponseRedirect(reverse('cus_login:home'))
                return render(request, 'User/home.html')
            else:
                return HttpResponse("Account has been diasabled!")
        else:
            print('x')
            return render(request, 'userlogin/index.html', {'err':'Invalid Login Details!','form':form})
    form=AuthenticationForm()
    print(form)
    return render(request, 'userlogin/index.html',{'form':form})

@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login.home'))
