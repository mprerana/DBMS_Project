from django.db import models

# Create your models here.


class Menu(models.Model):

    category_name = models.CharField(max_length=100, null=False)
    category_image = models.ImageField(upload_to='category_images', blank=True)

    class meta:
        unique_together = (
            'category_name',
            'category_image',
        )

    def __str__(self):
        return '%s' % self.category_name


class Cuisine_item(models.Model):

    item_name = models.CharField(max_length=100, null=False)
    item_category = models.ForeignKey(Menu, on_delete=models.PROTECT)
    item_desc = models.TextField(blank=True)
    item_image = models.ImageField(upload_to='Item_images',blank=True)
    item_price = models.IntegerField(blank=False, default=0)
    stock_quantity = models.IntegerField(default=0, null=False)

    class meta:
        indexes = [
            models.Index(fields=['item_name']),
            models.Index(fields=['item_category']),
        ]

    def __str__(self):
        return '%s ( %s )' % (self.item_name,self.item_category)
