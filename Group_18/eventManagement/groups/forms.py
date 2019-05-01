from django import forms
from .models import Group
from django.contrib.auth.models import User


class GroupsForm(forms.ModelForm):
    CHOICES = [[x.id, x.username] for x in User.objects.all()]
    to = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=CHOICES)
    message = forms.CharField(max_length=100)

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['creator']

    def save(self, request,commit=True):
        group = super(GroupsForm, self).save(commit=False)
        group.creator = request.user
        group.name = self.cleaned_data['name']
        group.description = self.cleaned_data['description']

        if commit:
            group.save()

        return 1