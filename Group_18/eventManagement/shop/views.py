from django.shortcuts import render
from django.db import connection
from django.views import generic
from shop.models import Product, PurchaseItem, Order
from events.models import event, regUser
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random
import string
from datetime import date
import datetime

from django.core.mail import send_mail

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


def get_user_pending_order(request):
    # get order for the correct user
    user_profile1 = get_object_or_404(User, username=request.user)
    order = Order.objects.filter(user=user_profile1, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required(login_url='/shop/login/')
def index(request):
    user1 = get_object_or_404(User, username=request.user)
    # event_list = event.objects.filter(registered_users=user1)
    user2 = regUser.objects.filter(user = user1)
    event_list = []
    for item in user2:
        event_list.append(item.event)
    print(user2)
    print(event_list)
    for event1 in event_list:
        all_products1 = event1.product.all()
    query = request.GET.get('q')
    if query:
        # all_products = all_products1.filter(name__icontains=query)
        event_list = event.objects.filter(name__icontains=query)
    else:
        # all_products = all_products1
        event_list = event_list
    return render(request, 'shop/index.html', {'event_list': event_list})


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('shop:index')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})
#@login_required(login_url='/med/login/')
#def detail(request, medicine_id):
 #   medicine = get_object_or_404(Medicine, pk=medicine_id)
  #  return render(request, 'med/detail.html', {'medicine': medicine})

def logout_view(request):
    #if request.method == 'POST':
    all_products = Product.objects.all()
    logout(request)
    return render(request, 'shop/index.html', {'all_medicines': all_products})


@login_required(login_url='/shop/login/')
def add_to_cart(request, **kwargs):
    user_profile1 = get_object_or_404(User, username=request.user)
    product = Product.objects.filter(id=kwargs.get('product_id', "")).first()
    #product = Product.objects.raw('select * from events_product where id= %s', kwargs.get('product_id', ""))[0]
    quantity = request.GET.get('quantity')
    # if product in request.user.user_profile.product.all():
    #     return redirect(reverse('shop:index'))
    purchase_item, status = PurchaseItem.objects.get_or_create(product=product, quantity=quantity)
    user_order, status = Order.objects.get_or_create(user=user_profile1, is_ordered=False)

    user_order.items.add(purchase_item)
    # if status:
        # generate a reference code
    user_order.ref_code = generate_order_id()
    purchase_item.ref_code = generate_order_id()
    user_order.save()
    purchase_item.save()

    return redirect(reverse('shop:index'))


def delete_from_cart(request, item_id):
    item_to_delete = PurchaseItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('shop:order_summary'))

def delete_order(request, order_id):
    order_to_delete = Order.objects.filter(pk=order_id)
    if order_to_delete.exists():
        order_to_delete[0].delete()
    return redirect(reverse('shop:checked'))

#@login_required()
#def CartView(request, **kwargs):
 #   user_profile = get_object_or_404(UserProfile, user=request.user)
  #  medicine =
    #model = Medicine
    #fields = ['name', 'pharmacy', 'description', 'mfg_date', 'mfg_date', 'exp_date', 'price']


def checkout(request, order_id):
    order_purchased = Order.objects.filter(pk=order_id)
    order_purchased.date_ordered = datetime.datetime.now()
    address = request.GET.get('address')
    email = request.GET.get('email')
    order_purchased.update(email=email)
    order_purchased.update(billing_add=address)
    # order_items = order_to_purchase.items.all()
    order_purchased.update(is_ordered=True)
    order_purchased.update(date_ordered=datetime.datetime.now())
    # send_mail("Your quickwell.com order has been confirmed","Thankyou for shopping at Quickwell!!...you will receive your order in 3 days","quickwelldoctor@gmail.com", [order_purchased[0].email])

    context = {
        'order': order_purchased[0],
    }
    return render(request, 'shop/checkout.html', context)


def finalPrice(request, order_id):

    order_to_purchase = Order.objects.filter(pk=order_id)
    # query = request.GET.get()
    # print(query)
    # order_to_purchase.is_ordered = True

    context = {
        'order': order_to_purchase[0],
    }
    return render(request, 'shop/order.html', context)

def send(request):
    if request.POST:
        id = request.POST['id']
        quantity = request.POST.get('qq')
        print(quantity)
        Prod = PurchaseItem.objects.filter(pk=id)
        print(Prod)
        Prod.update(quantity=quantity)
        # Prod.save()
        print(id)
        context = {
            'product' : Prod
        }
        return render(request, 'shop/send.html', context)



@login_required(login_url='/shop/login')
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shop/order_summary.html', context)
#
#
#
# def get_user_checked_order(request):
#     # get order for the correct user
#     user_profile = get_object_or_404(UserProfile, user=request.user)
#     order = Order.objects.filter(user=user_profile, is_ordered=True)
#     if order.exists():
#         # get the only order in the list of filtered orders
#         return order
#     return 0
#
#
# @login_required(login_url='/med/login')
# def checked(request, **kwargs):
#     checked_order = get_user_checked_order(request)
#     context = {
#         'order': checked_order
#     }
#     return render(request, 'med/order_checked.html', context)


@login_required(login_url='/shop/login')
def checked(request, **kwargs):
    user_profile1 = get_object_or_404(User, username=request.user)

    order = Order.objects.filter(user=user_profile1, is_ordered=True)
    order.update()
    context = {
        'order': order
    }

    return render(request, 'shop/order_checked.html', context)


def get_registered_events(request):
    events_registered = event.objects.filter(user_name=request.user)




#def my_profile(request):
#	my_user_profile = UserProfile.objects.filter(user=request.user).first()
#	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
#	context = {
#		'my_orders': my_orders
#	}

#	return render(request, "profile.html", context)


