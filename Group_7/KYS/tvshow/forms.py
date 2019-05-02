from django import forms
from .models import TVShow, Season, Episode

class seriesForm(forms.ModelForm):
    class Meta:
        model = TVShow
        fields = ('titleName', 'seriesReview', 'GENRE', 'language', 'seriesSummary')

class seasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ('seasonNum',)

class episodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ('episodeNum', 'episodeName', 'releaseDate', 'cast', 'episodeReview', 'runTime',
                  'episodePoster', 'episodeSummary', )