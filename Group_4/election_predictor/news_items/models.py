from django.db import models
from authentication.models import Usertype


class Query(models.Model):
    query = models.CharField(max_length=200, primary_key=True)
    query_fk = models.ForeignKey(Usertype, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.query


class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    is_active = models.BooleanField(default=False)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Region(models.Model):
    choices = (('Andhra+Pradesh', 'Andhra Pradesh'), ('Arunachal+Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'),
               ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'),
               ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal+Pradesh', 'Himachal Pradesh'),
               ('Jammu+and+Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'),
               ('Kerala', 'Kerala'), ('Madya+Pradesh', 'Madya Pradesh'), ('Maharashtra', 'Maharashtra'),
               ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'),
               ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'),
               ('Tamil+Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'),
               ('Uttaranchal', 'Uttaranchal'), ('Uttar+Pradesh', 'Uttar Pradesh'), ('West+Bengal', 'West Bengal'),
               ('Andaman+and+Nicobar+Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'),
               ('Dadar+and+Nagar+Haveli', 'Dadar and Nagar Haveli'), ('Daman+and+Diu', 'Daman and Diu'),
               ('Lakshadeep', 'Lakshadeep'), ('Pondicherry', 'Pondicherry'),)
    region = models.CharField(max_length=200, choices=choices)