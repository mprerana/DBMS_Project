from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
from django.contrib.auth.models import User

class funds(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    started_on = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    report = models.CharField(max_length=2048)
    place = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    target = models.IntegerField(validators=[MinValueValidator(100000),])

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(funds, on_delete=models.CASCADE)
    message = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Images(models.Model):
    post = models.ForeignKey(funds, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="reliffunds",)

class updates(models.Model):
    post = models.ForeignKey(funds, on_delete=models.CASCADE)
    update = models.CharField(max_length=1024)
    time = models.DateTimeField()
