from django.db import models

# Create your models here.


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    Subject = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Message = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
