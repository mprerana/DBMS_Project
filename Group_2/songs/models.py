from django.db import models

# Create your models here.
class Songs_List(models.Model):
    song = models.CharField(max_length=150,null=True,blank=True)
    type = models.CharField(max_length=150,null=True)
    artist_album = models.CharField(max_length=150, null=True)
    released = models.CharField(max_length=150,null=True)
    rating = models.CharField(max_length=150,null=True)
    poster = models.URLField(max_length=200, null=True)
    runtime = models.CharField(max_length=150,null=True)
    #trailer = models.URLField(max_length=200, null=True)

