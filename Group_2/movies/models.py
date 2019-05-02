from django.db import models

# Create your models here.


class Movie_list(models.Model):
    movie = models.CharField(max_length=150,null=True,blank=True)
    genre = models.CharField(max_length=150,null=True)
    released = models.CharField(max_length=150,null=True)
    imdb_rating = models.CharField(max_length=150,null=True)
    poster = models.URLField(max_length=200, null=True)
    runtime = models.CharField(max_length=150,null=True)
    trailer = models.URLField(max_length=200, null=True)


