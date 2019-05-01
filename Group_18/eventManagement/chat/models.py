from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="toreceiver", default=1)
    roomname = models.CharField(max_length=100)

    def __str__(self):
        return self.author.username

    def last_10_messages(x):
        abc = Message.objects.filter(roomname = x)
        return abc
