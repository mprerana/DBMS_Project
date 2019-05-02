from django import forms
from show.models import GENRE,language,Show


class search_bar(forms.Form):
    search_query = forms.CharField(label='',max_length=100)
    search_ty = forms.ChoiceField(label='',choices=[(x, x) for x in ['Movies','Cast','Tv shows']])
