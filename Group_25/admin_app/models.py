from django.db import models
import datetime

# Create your models here.


class Queue_order_item(models.Model):

    order_id = models.IntegerField()
    item_id = models.IntegerField()

    def __str__(self):
        return '%d %d' % (self.order_id, self.item_id)
