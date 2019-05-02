from django.db import models
from show.models import language, GENRE, review
from cast.models import cast, director, producer


# Create your models here.

class TVShow(models.Model):
    titleName = models.CharField(max_length=120)
    seriesReview = models.ForeignKey(review, on_delete=models.SET_NULL, blank=True, null=True)
    GENRE = models.ManyToManyField(GENRE)
    language = models.ManyToManyField(language)
    seriesSummary = models.CharField(max_length=2500)

    seriesPoster = models.CharField(max_length=1000)
    # seriesPoster = models.ImageField(upload_to='series_posters', blank=True)
    seriesViewCount = models.IntegerField(default= 0)

    def __str__(self):
        return self.titleName


class Season(models.Model):
    seasonNum = models.IntegerField(unique=True)
    def season_id(self):
        return seasonNum
    def __str__(self):
        return str('Season '+ str(self.seasonNum))


class Episode(models.Model):
    episodeNum = models.IntegerField()
    series = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    episodeName = models.CharField(max_length=50, null= True)
    releaseDate = models.CharField(max_length=100)
    cast = models.ManyToManyField(cast)
    episodeReview = models.ForeignKey(review, on_delete=models.SET_NULL, blank=True, null=True)
    runTime = models.DurationField()
    episodePoster = models.CharField(max_length=1000)
    # episodePoster = models.ImageField(upload_to='series_posters/episode_posters', blank=True)
    episodeSummary = models.CharField(max_length=2500)

    def __str__(self):
        # if self.episodeName == None :
        #     return str('Episode '+ str(self.episodeNum))
        return self.episodeName
