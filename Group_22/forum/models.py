from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class forumdetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    request_header = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    amount = models.IntegerField(validators=[MinValueValidator(50000),])
    pic = models.ImageField(upload_to='requests', default='static/userlogin/images/default-img.png')
    by_date = models.DateField()

    def __str__(self):
        return self.request_header

class commentinfo(models.Model):
    to = models.ForeignKey(forumdetails, on_delete=models.CASCADE)
    message = models.CharField(max_length=1024)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
