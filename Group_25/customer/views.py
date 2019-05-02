from django.shortcuts import render,HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from order.models import Cust_cart_item
from customer.models import Customer

from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    items = Cust_cart_item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'customer/home.html', context=context)


def user_registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid() and not form.errors:
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('customer/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'customer/register.html', {'form': form})


def activate(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        message = 'Your account has been activated! Now you can login your account.'
        return render(request, 'customer/login.html', {'email_confirmed': message})

    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('customer:home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login but failed!")
            print("Username: {} and password {}".format(username,password))
            return render(request, 'customer/login.html', {'msg':'Invalid Details Provided!'})
    else:

        return render(request, 'customer/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('customer:home'))


@login_required
def update_profile(request):

    if request.method == 'POST':

        customer = Customer.objects.get(user__username=request.user.username)
        customer.user.first_name = request.POST['fname']
        customer.user.last_name = request.POST['lname']
        customer.user.email = request.POST['email']
        customer.cust_phone = request.POST['phone']
        customer.cust_street = request.POST['street']
        customer.cust_house_no = request.POST['house']
        customer.cust_city = request.POST['city']
        customer.cust_zipcode = request.POST['zip']

        customer.save()
        context = {
            'message': 'Profile Updated Successfully!',
            'customer': customer
        }
        return render(request, 'customer/profile.html', context=context)

    else:
        customer = Customer.objects.get(user__username=request.user.username)
        context = {
            'customer': customer
        }
        return render(request, 'customer/profile.html', context=context)


def contact(request):
    return render(request, 'customer/contact.html')



# def user_registration(request):
#
#     if request.method == 'POST':
#
#         customer = User()
#         customer.username = request.POST['uname']
#         customer.first_name = request.POST['fname']
#         customer.last_name = request.POST['lname']
#         customer.email = request.POST['email']
#         customer.set_password(request.POST['pswd'])
#         customer.save()
#         #registered_customer = Customer.objects.get(user=customer)
#         # cust_cart = Cust_Cart.objects.create(cart_id=registered_customer.id)
#         # cust_cart.save()
#
#         context = {'message': "Registered Succesfully!"}
#         return render(request, 'customer/register.html', context=context)
#     else:
#         return render(request, 'customer/register.html')
