from django.db import models

# Create your models here.
class Games_List(models.Model):
    game = models.CharField(max_length=150,null=True,blank=True)
    genre = models.CharField(max_length=150,null=True)
    released = models.CharField(max_length=150,null=True)
    rating = models.CharField(max_length=150,null=True)
    poster = models.URLField(max_length=200, null=True)
    developer = models.CharField(max_length=150,null=True)
    trailer = models.URLField(max_length=200, null=True)

