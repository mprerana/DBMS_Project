
from django.contrib import admin
from .models import  AccountBalance,Statement,Pending_transactions,Pending_redeem

admin.site.register(AccountBalance)
admin.site.register(Statement)
admin.site.register(Pending_transactions)
admin.site.register(Pending_redeem)
# Register your models here.
