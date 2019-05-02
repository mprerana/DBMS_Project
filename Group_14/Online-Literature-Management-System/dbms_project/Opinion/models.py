from django.db import models
from django.contrib.auth.models import User
from Literature.models import Work
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    book = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    timestamp = models.CharField(max_length=100)

    class Meta:
        indexes = (models.Index(fields=["user", "book"]),)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    book = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=False)
    timestamp = models.CharField(max_length=100)
    content = models.TextField(blank=False,)

    class Meta:
        indexes = (models.Index(fields=["user", "book"]),)