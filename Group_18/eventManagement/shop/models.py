from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     event = models.ForeignKey(event, null=True, on_delete=models.CASCADE)
#     description = models.CharField(max_length=1000, default='0000000')
#     image = models.ImageField(blank=True)
#     price = models.FloatField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    # event = models.ForeignKey(event, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='0000000', null=True)
    image = models.ImageField(blank=True)
    price = models.FloatField()


class PurchaseItem(models.Model):
    ref_code = models.CharField(max_length=15, default='0000000')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, unique=None)
    quantity = models.IntegerField(null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(null=True)
    date_ordered = models.DateTimeField(null=True)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(PurchaseItem)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True)
    billing_add = models.CharField(max_length=1000, blank=True)
    email = models.CharField(max_length=100, default='0000000', null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_no_of_purchase(self):
        sum1 = 0;
        for item in self.items.all():
            sum1 = sum1+1;
        return sum1;

    def get_cart_total(self):
        sum = 0 ;
        for item in self.items.all():
            sum = sum + ((item.product.price)*(item.quantity))
        return sum

    def get_estimated_date(self):
        date1 = self.date_ordered;
        date1 = date1 + datetime.timedelta(days=3);
        return date1