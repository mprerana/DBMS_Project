from django.contrib import admin
from .models import PaytmHistory


class PaytmHistoryAdmin(admin.ModelAdmin):
    list_display = ('ORDERID', 'MID', 'TXNAMOUNT', 'STATUS')

admin.site.register(PaytmHistory, PaytmHistoryAdmin)
