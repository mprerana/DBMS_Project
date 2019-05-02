from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class USER(models.Model):
    user_data = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics', blank='True', null=True, )
    mobile_no = models.CharField(max_length=10, blank='True', null=True, )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.user_data.username)

    @receiver(post_save, sender=User)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            USER.objects.create(user_data=instance)


class FOLLOW(models.Model):
    user = models.ForeignKey(USER, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='user')
    follower = models.ForeignKey(USER, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='follower')

    class Meta:
        indexes = (models.Index(fields=["user", "follower"]),)
        unique_together = (('user', 'follower'),)
