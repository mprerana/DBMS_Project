from django.shortcuts import render, reverse, HttpResponseRedirect
from product.models import Cuisine_item,Menu
from order.models import *
from customer.models import *
from django.shortcuts import get_object_or_404
from product.forms import ProductForm
from order.forms import OrderForm
from payments.models import Cust_order_payment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
status_options = {'0': 'Processing',
                  '1': 'Confirmed',
                  '2': 'Cancelled', }

order_item_status = {'0': 'Processing',
                     '1': 'Prepared',}

payment_status_options = {'0': 'Processing',
                          '1': 'Completed',
                          '2': 'Failed',}


def index(request):

    return render(request, 'admin_app/admin.html')


def product_report(request):

    item_list = Cuisine_item.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(item_list, 4)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {
        'items': items
    }
    return render(request, 'admin_app/product_report.html', context=context)


def order_report(request):

    order_list = Cust_order.objects.all()
    status_list = []

    for order in order_list:
        status_list.append(status_options[str(order.order_status)])

    context = {
        'zipped_data': zip(order_list, status_list)
    }

    return render(request, 'admin_app/order_report.html', context=context)


def update_product(request, item_id):

    if request.method == 'POST':
        item = get_object_or_404(Cuisine_item, pk=item_id)
        product_form = ProductForm(request.POST, request.FILES,instance=item)

        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_app:product_report'))
        else:
            print(product_form.errors)
    else:
        item = get_object_or_404(Cuisine_item, pk=item_id)
        product_form = ProductForm(instance=item)
        context = {
            'product_form': product_form,
            'item_id': item_id,
        }
        return render(request, 'admin_app/product_form.html', context=context)


def check_order_payment(request, order_id):

    payment = get_object_or_404(Cust_order_payment, order_id=order_id)

    status = payment_status_options[str(payment.payment_status)]

    context = {
        'payment': payment,
        'status': status,
    }

    return render(request, 'admin_app/order_report.html', context=context)


def update_order(request, order_id):

    order = get_object_or_404(Cust_order, pk=order_id)
    order_form = OrderForm(request.POST or None, instance=order)

    if request.method == 'POST':

        if order_form.is_valid():
            order_form.save()
            return HttpResponseRedirect(reverse('admin_app:order_report'))
        else:
            print(order_form.errors)
    else:
        context = {
            'order_form': order_form,
            'order_id': order_id,
        }

        return render(request, 'admin_app/order_form.html', context=context)


def check_order_items(request, order_id):

    item_list = Cust_order_item.objects.filter(order_id=order_id)

    item_status = []
    for item in item_list:
        item_status.append(order_item_status[str(item.order_item_status)])

    zipped_data = zip(item_list, item_status)

    context = {
        'zipped_data2': zipped_data
    }

    return render(request, 'admin_app/order_report.html', context=context)
