from django import forms
from .models import event,invitation,review,categories
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    CHOICES = [[x.id, x.username] for x in User.objects.all()]
    invite_users = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=CHOICES)
    message = forms.CharField(max_length=100)

    class Meta:
        model = event
        fields = '__all__'
        exclude = ['user', 'registered_users',]



    def save(self, request, commit=True):

        f = super(EventForm, self).save(commit=True)
        f.user = request.user
        f.name = self.cleaned_data['name']
        f.description = self.cleaned_data['description']
        f.venue = self.cleaned_data['venue']
        f.city = self.cleaned_data['city']
        f.state = self.cleaned_data['state']
        f.private = self.cleaned_data['private']
        f.start_date = self.cleaned_data['start_date']
        f.start_time = self.cleaned_data['start_time']
        f.end_date = self.cleaned_data['end_date']
        f.end_time = self.cleaned_data['end_time']
        if commit:
            f.save()

        return f



class ReviewForm(forms.ModelForm):


    class Meta:
        model = review
        fields = '__all__'
        exclude = ['by', 'event','rating','date']
