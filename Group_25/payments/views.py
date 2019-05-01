from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404, reverse
from order.models import Cust_order
from payments.models import Cust_order_payment
from payments.utils import unique_payment_id_generator
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.db import connection
from django.utils import timezone


# Create your views here.


payment_status_options = {'0': 'Processing',
                          '1': 'Completed',
                          '2': 'Failed', }


@csrf_exempt
def payment_done(request):

    order_id = request.session.get('order_id')
    payment_id = request.session.get('payment_id')
    order = get_object_or_404(Cust_order, id=order_id)
    cust_id = order.cust_id.id

    payment = get_object_or_404(Cust_order_payment, payment_id=payment_id)
    payment.payment_status = 1
    payment.payment_date = timezone.now()
    payment.save()
    status = payment_status_options[str(payment.payment_status)]

    cursor = connection.cursor()
    try:
        cursor.callproc('cart_item_to_order_item', [int(order_id), int(cust_id)])

    finally:
        cursor.close()

    context = {
        'payment': payment,
        'status': status
    }
    return render(request, 'payments/done.html', context=context)


@csrf_exempt
def payment_canceled(request):

    payment_id = request.session.get('payment_id')
    payment = get_object_or_404(Cust_order_payment, payment_id=payment_id)
    payment.payment_status = 2
    payment.save()
    status = payment_status_options[str(payment.payment_status)]

    context = {
        'payment': payment,
        'status': status
    }
    return render(request, 'payments/canceled.html', context=context)


def payment_process(request):

    order_id = request.session.get('order_id')
    order = get_object_or_404(Cust_order, id=order_id)
    host = request.get_host()

    payment = Cust_order_payment.objects.create(payment_status=0,
                                                order_id=order,
                                                payment_date=timezone.now(),
                                                customer_id=order.cust_id.user.username)
    payment.save()

    request.session['payment_id'] = payment.payment_id

    paypal_dict = {

      'business': settings.PAYPAL_RECEIVER_EMAIL,
      'amount': '%.2f' % order.order_total_price,
      'item_name': 'Order {}'.format(order.id),
      'invoice': str(order.id),
      'currency_code': 'INR',
      'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
      'return_url': 'http://{}{}'.format(host,reverse('payments:done')),
      'cancel_url': 'http://{}{}'.format(host, reverse('payments:canceled')),

    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'payments/process.html', context=context)
