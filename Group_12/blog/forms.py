from django import forms
from django.core.exceptions import ValidationError
from .models import Blog, Comment, interest
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from dal import autocomplete


class story(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    interest = forms.ModelChoiceField(
        queryset=interest.objects.all(),
        widget=autocomplete.ModelSelect2(url='blog:name-autocomplete',
                                         attrs={
                                             'data-placeholder': 'Interest-name',
                                             'data-minimum-input-length': 1,
                                         })
    )

    class Meta:
        model = Blog
        fields = (
            'heading', 'interest'
        )

    def clean_heading(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        return heading


class comment(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 2}))

    class Meta:
        model = Comment
        fields = (
            'content',
        )
