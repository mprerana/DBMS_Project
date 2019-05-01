from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from movie_booking import settings
from payment import Checksum
from payment.Checksum import generate_checksum, verify_checksum, generate_checksum_by_str, verify_checksum_by_str
#from intranet import models
#from intranet.models import Borrowers
from payment.models import PaytmHistory



def pay(request):

    merchantMid = settings.PAYTM_MERCHANT_ID
    merchantKey = settings.PAYTM_MERCHANT_KEY
    order_id = Checksum.__id_generator__()
    channelId = 'WEB'
    #custId = request.POST['cnumber']
    #txnAmount = request.POST['fine']

    custId = "fds"
    txnAmount = '180'

    website = 'WEBSTAGING'
    industryTypeId = 'Retail'
    callbackUrl = "http://127.0.0.1:8001/1/payment/check"

    paytmParams = {
        'MID': merchantMid,
        'ORDER_ID': order_id,
        'CUST_ID': custId,
        'INDUSTRY_TYPE_ID': industryTypeId,
        'CHANNEL_ID':channelId,
        'TXN_AMOUNT': txnAmount,
        'WEBSITE':website,
        'CALLBACK_URL': callbackUrl,
    }
    paytmChecksum = generate_checksum(paytmParams, merchantKey)
    paytmParams['CHECKSUMHASH'] = paytmChecksum
    context = {'paytmDict': paytmParams}
    return render(request, 'form1.html', context)

@csrf_exempt
def check(request):
    merchantKey = settings.PAYTM_MERCHANT_KEY
    if request.method == 'POST':
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        if 'CHECKSUMHASH' in data_dict.keys():
            paytmChecksum = request.POST['CHECKSUMHASH']
        else:
            paytmChecksum = ""

        isValidChecksum = verify_checksum(data_dict, merchantKey, paytmChecksum)
        context = {'paytmDict': data_dict}
        if (isValidChecksum):
            PaytmHistory.objects.create(**data_dict)
            return render(request, 'form2.html', context)
        else:
            return HttpResponse("Checksum verify failed")
    else:
        return HttpResponse(status= 200)


def status(request):
    data_dict = {}
    for key in request.POST:
        data_dict[key] = request.POST[key]
    print(data_dict)
    context = {'resultDict': data_dict}
    return render(request, 'status.html', context )


def pay_fine(request):
    return render(request, 'pay_fine.html')