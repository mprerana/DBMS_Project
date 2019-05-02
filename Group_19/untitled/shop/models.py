from django.db import models
from django.urls import reverse

class Document(models.Model):
    image = models.FileField(upload_to='documents/')



