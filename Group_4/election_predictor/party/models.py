from django.db import models
from authentication.models import Party


class PaymentDetails(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.FloatField(null=True)

    def __str__(self):
        return self.transaction_id


class SecretKey(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE,primary_key=True)
    sk = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.sk
