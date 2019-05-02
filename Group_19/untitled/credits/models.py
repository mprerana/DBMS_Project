from django.db import models
import uuid
from random import seed
from django.contrib.auth.models import User

class AccountBalance(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    # fullname = models.CharField(max_length=30, null=True)
    balance = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.user.username


class Statement(models.Model):
    # last1 = models.FloatField(default=0)
    # transaction_id_1 = models.CharField(max_length=12, unique=True)
    # date1 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    # last2 = models.FloatField(default=0)
    # transaction_id_2 = models.CharField(max_length=12, unique=True)
    # date2 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    # last3 = models.FloatField(default=0)
    # transaction_id_3 = models.CharField(max_length=12, unique=True)
    # date3 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    # last4 = models.FloatField(default=0)
    # transaction_id_4 = models.CharField(max_length=12, unique=True)
    # date4 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    # last5 = models.FloatField(default=0)
    # transaction_id_5 = models.CharField(max_length=12, unique=True)
    # date5 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField(default=0)
    transaction_id = models.CharField(max_length=12)
    user = models.CharField(max_length=30,null=False)

    def __str__(self):
        return str(self.user)


def random_transaction_id():
    seed()
    transaction_id = "ADD" + uuid.uuid4().hex[:9].upper()
    return transaction_id


class Pending_transactions(models.Model):
    transaction_date = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=12, default=0, unique=True)
    transaction_id = models.CharField(max_length=14, default=random_transaction_id())
    user = models.CharField(max_length=30,null=False)
    pending_amount = models.FloatField(null=False)

    def __str__(self):
        return str(self.user)


class Pending_redeem(models.Model):
    transaction_date = models.DateTimeField(auto_now=True)
    code = models.IntegerField(default=666781, unique=True)
    transaction_id = models.CharField(max_length=14, default=uuid.uuid4().hex[:12].upper())
    user = models.CharField(max_length=30,null=False)
    redeem_amount = models.FloatField(null=False)

    def __str__(self):
        return str(self.user)
