from django import forms
from .import models

class CreatePackage(forms.ModelForm):
    class Meta:
        model = models.package
        fields = ['user_id','package_id','origin','destination','train','hotel','no_of_days','money']
