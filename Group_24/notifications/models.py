from django.db import models
from accounts.models import UserProfile

# Create your models here.
class NotificationList(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=250)
    read = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields = ['user',]),
        ]
