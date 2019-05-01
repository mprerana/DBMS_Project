from django import forms

from .models import Query, Region


class FeedForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('query',)


class RegionForm(forms.ModelForm):
    #fields = forms.ChoiceField(widget=forms.Select, choices=choices)
    #select = forms.CharField(widget=forms.Select(choices=choices))
    class Meta:
        model = Region
        choices = (('Andhra+Pradesh','Andhra Pradesh'), ('Arunachal+Pradesh','Arunachal Pradesh'), ('Assam','Assam'),
                   ('Bihar','Bihar'), ('Chhattisgarh','Chhattisgarh'), ('Delhi','Delhi'), ('Goa','Goa'),
                   ('Gujarat','Gujarat'), ('Haryana','Haryana'), ('Himachal+Pradesh','Himachal Pradesh'),
                   ('Jammu+and+Kashmir','Jammu and Kashmir'), ('Jharkhand','Jharkhand'), ('Karnataka','Karnataka'),
                   ('Kerala','Kerala'), ('Madya+Pradesh','Madya Pradesh'), ('Maharashtra','Maharashtra'),
                   ('Manipur','Manipur'), ('Meghalaya','Meghalaya'), ('Mizoram','Mizoram'), ('Nagaland','Nagaland'),
                   ('Orissa','Orissa'), ('Punjab','Punjab'), ('Rajasthan','Rajasthan'), ('Sikkim','Sikkim'),
                   ('Tamil+Nadu','Tamil Nadu'), ('Telagana','Telagana'), ('Tripura','Tripura'),
                   ('Uttaranchal','Uttaranchal'), ('Uttar+Pradesh','Uttar Pradesh'), ('West+Bengal','West Bengal'),
                   ('Andaman+and+Nicobar+Islands','Andaman and Nicobar Islands'), ('Chandigarh','Chandigarh'),
                   ('Dadar+and+Nagar+Haveli','Dadar and Nagar Haveli'), ('Daman+and+Diu','Daman and Diu'),
                   ('Lakshadeep','Lakshadeep'), ('Pondicherry','Pondicherry'), )
        region = forms.TypedChoiceField(widget=forms.Select(choices=choices))
        exclude=()