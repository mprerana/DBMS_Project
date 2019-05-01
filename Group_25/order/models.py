from django.db import models
from customer.models import Customer
from product.models import Cuisine_item
import datetime
from django.utils import timezone

# Create your models here.

status = (('0', 'Processing'),
          ('1', 'Confirmed'),
          ('2', 'Cancelled'),)

order_item_status = (('0', 'Processing'),
                      ('1', 'Prepared'))


class Cust_Cart(models.Model):

    cart_id = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return '%s' % self.cart_id


class Cust_cart_item(models.Model):

    cart_id = models.ForeignKey(Cust_Cart, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(Cuisine_item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=0, null=False)
    item_price = models.FloatField(default=0, null=False)

    def __str__(self):
        return '%s' % self.cart_item


class Cust_order(models.Model):

    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_total_price = models.FloatField(null=False, default=0)
    order_date = models.DateTimeField(null=False)
    order_status = models.CharField(choices=status, max_length=50, default=0)

    class Meta:
        unique_together = (
            'id',
            'cust_id',
        )

    def __str__(self):
        return '%d %s ' % (self.id, self.cust_id.user.username)


class Cust_order_item(models.Model):

    order_id = models.ForeignKey(Cust_order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Cuisine_item, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    price = models.FloatField(default=0, null=False)
    order_item_status = models.CharField(choices=order_item_status, max_length=50, default=0)

    def __str__(self):
        return '%s' % self.order_id






