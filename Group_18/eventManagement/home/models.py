from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class EmailConfirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        EmailConfirm.objects.create(user=instance)
    instance.emailconfirm.save()

class user_rating(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(null=True, default=0)

    def post_save_user_rating_create(sender, instance, created, *args, **kwargs):
        if created:
            user_rating.objects.get_or_create(user=instance)

    post_save.connect(post_save_user_rating_create, sender=User)

    def __str__(self):
        return self.user.username+" "+(str)(self.rating)

