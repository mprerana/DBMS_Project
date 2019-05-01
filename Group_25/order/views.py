from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect, reverse
from order.models import Cust_Cart,Cust_cart_item,Cust_order,Cust_order_item
from product.models import Cuisine_item
from customer.models import Customer
from payments.models import Cust_order_payment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db import connection

# Create your views here.

status_options = {'0': 'Processing',
                  '1': 'Confirmed',
                  '2': 'Cancelled', }

payment_status_options = {'0': 'Not done!',
                          '1': 'Completed',
                          '2': 'Failed',}

@login_required
def check_cart_items(request):
    username = request.user.username
    customer = Customer.objects.get(user__username=username)

    cart_items = Cust_cart_item.objects.filter(cart_id=customer.id)

    if cart_items:
        context = {
            'cart_items': cart_items
        }
        return render(request, 'order/cart.html', context=context)
    else:
        context = {
            'message': 'Cart is Empty!'
        }
        return render(request, 'order/cart.html', context=context)


@login_required
def add_to_cart(request, item_id):

    if request.method == 'POST':

        item_quantity = request.POST['qnty']
        username = request.user.username
        customer = Customer.objects.get(user__username=username)

        cart_id = get_object_or_404(Cust_Cart, pk=customer.id)
        item = get_object_or_404(Cuisine_item, pk=item_id)
        try:

            old_cart_item = Cust_cart_item.objects.get(cart_id=cart_id,cart_item=item)
            old_cart_item.item_quantity = int(int(item_quantity) + int(old_cart_item.item_quantity))
            old_cart_item.item_price = int(old_cart_item.item_quantity) * float(item.item_price)
            old_cart_item.save()
            return HttpResponseRedirect(reverse('order:cart'))

        except:

            new_item_price = float(float(item.item_price) * int(item_quantity))
            cart_item = Cust_cart_item.objects.create(cart_id=cart_id,
                                                      cart_item=item,
                                                      item_price=new_item_price,
                                                      item_quantity=item_quantity)
            cart_item.save()
            return HttpResponseRedirect(reverse('order:cart'))

    return render(request, 'product/base_items.html')


@login_required
def remove_cart_item(request, cart_item_id):

    username = request.user.username
    customer = Customer.objects.get(user__username=username)

    cart_id = customer.id
    cursor = connection.cursor()
    try:
        cursor.callproc('remove_cart_item',[int(cart_id), int(cart_item_id)])

    finally:
        cursor.close()

    return HttpResponseRedirect(reverse('order:cart'))


@login_required
def order(request):
    username = request.user.username
    customer = Customer.objects.get(user__username=username)

    cart_items = Cust_cart_item.objects.filter(cart_id=customer.id)

    if cart_items:
        context = {
            'item_list': cart_items,
        }
        return render(request, 'order/order_summary.html', context=context)

    else:
        context = {
            'message': 'Cart is Empty!'
        }
        return render(request, 'order/cart.html', context=context)


@login_required
def order_items(request):

    username = request.user.username
    customer = Customer.objects.get(user__username=username)

    item_list = Cust_cart_item.objects.filter(cart_id=customer.id)

    total_price = 0

    if item_list:
        for item in item_list:
            total_price = total_price + item.item_price

        order = Cust_order.objects.create(cust_id=customer,
                                          order_total_price=total_price,
                                          order_date=timezone.now(),
                                          order_status=0)
        status = status_options[str(order.order_status)]
        order.save()

        request.session['order_id'] = order.id
        item_list = Cust_order_item.objects.filter(order_id=order)

        context = {
            'order': order,
            'item_list': item_list,
            'status': status,
        }
        return HttpResponseRedirect(reverse('payments:process'))

    else:

        context = {
            'message': 'Cart is Empty!'
        }
        return render(request, 'order/cart.html', context=context)


@login_required
def order_history(request):

    customer = Customer.objects.get(user__username=request.user.username)
    cust_id = customer.id

    cursor = connection.cursor()
    try:
        cursor.callproc('order_history', [int(cust_id)])
        order_list = cursor.fetchall()
    finally:
        cursor.close()

    payments = Cust_order_payment.objects.filter(customer_id=customer.user.username)

    status = []
    customer_ids = []
    payment_status = []

    for order in order_list:
        customer_ids.append(str(request.user.username))
        status.append(status_options[str(order[4])])

    for payment in payments:
        payment_status.append(payment_status_options[str(payment.payment_status)])

    context = {
        'zipped_data1': zip(order_list, status, customer_ids),
        'zipped_data2': zip(payments, payment_status)
    }

    return render(request, 'order/order-histoy.html', context=context)


def order_history_items(request, order_id):

    item_list = Cust_order_item.objects.filter(order_id=order_id)

    context = {
        'item_list': item_list,
    }

    return render(request, 'order/order-histoy.html', context=context)


def check_order_payment(request, order_id):

    payment = get_object_or_404(Cust_order_payment, order_id=order_id)

    status = payment_status_options[str(payment.payment_status)]

    context = {
        'payment': payment,
        'status': status,
    }
    return render(request, 'order/order-histoy.html', context=context)
