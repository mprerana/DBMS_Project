from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth.models import User


# class service(models.Model):
#
#     service_name = models.CharField(max_length=200,primary_key=True)
#     # review_count = models.IntegerField(null=False)
#     # avg_rating = models.FloatField(null=False,default=0)
#     def __str__(self):
#         return self.service_name
#
# class rate(models.Model):
#     rating_choices = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     )
#
#     service_name = models.ForeignKey(service,on_delete=models.PROTECT,null=True)
#     user_name = models.CharField(max_length=200)
#     rating = models.IntegerField(choices=rating_choices)
#     comment = models.TextField()
#     published_date = models.DateTimeField(blank=True, null=True)

class rate(models.Model):
    rating_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    # service_choices = (
    #     ('Flight','Flight'),
    #     ('Hotel','Hotel'),
    #)
    #service_type = models.CharField(choices=service_choices,max_length=200,default='Flight')
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    user = models.CharField(max_length=200,null=True)
    service_name = models.CharField(max_length=200)
    rating = models.IntegerField(choices=rating_choices)
    comment = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    #likes = models.IntegerField(default=0)


