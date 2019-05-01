from django.db import models

# Create your models here.
class adv(models.Model):
    adv_id = models.IntegerField()
    expiry=models.IntegerField()
    tenant_id=models.IntegerField()
    tenant_name=models.CharField(max_length=255)
    floor=models.IntegerField()
    ad_desc=models.CharField(max_length=255)
    deal=models.FloatField()
    image=models.ImageField(default='',upload_to='')

