from django.db import models

# Create your models here.
class tv_series_list(models.Model):
    tv_series = models.CharField(max_length=150,null=True,blank=True)
    genre = models.CharField(max_length=150,null=True)
    year = models.CharField(max_length=100, null=True)
    released = models.CharField(max_length=150,null=True)
    imdb_rating = models.CharField(max_length=150,null=True)
    poster = models.URLField(max_length=200, null=True)
    seasons = models.CharField(max_length=150,null=True)
    trailer = models.URLField(max_length=200, null=True)

