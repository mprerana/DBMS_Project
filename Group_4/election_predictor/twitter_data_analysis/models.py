from django.db import models
from authentication.models import Party
# Create your models here.
class tweets(models.Model):
	hashtag = models.CharField(max_length = 200);
	tweet = models.TextField(blank = True, null = True);
	party = models.ForeignKey(Party,on_delete=models.CASCADE)
	is_pro = models.BooleanField(default = False)