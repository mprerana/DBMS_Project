from django import forms
from . models import GENRE,language,Show,review


class languageForm(forms.ModelForm):

    class Meta:
        model = language
        fields = ('languages',)

class genreForm(forms.ModelForm):

    class Meta:
        model = GENRE
        fields = ('genres',)

class show_update_form(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('titleName','releaseDate','storyLine','budget','BoxOfficeCollection')

class rate_review(forms.ModelForm):
    ratings = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    Review = forms.CharField(label='Review', max_length=1000)
    rating = forms.ChoiceField(choices=ratings)
