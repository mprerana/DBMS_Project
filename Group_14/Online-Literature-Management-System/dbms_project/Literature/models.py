from django.db import models
from User.models import USER
from django.contrib.auth.models import User
import os

def content_file_name(instance, filename):
    return os.path.join('files', instance.uploader.username, instance.work_title, filename)

def content_thumbnail_name(instance, filename):
    return os.path.join('thumbnails', instance.uploader.username, instance.work_title, filename)



class Blog(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=150)
    blog_content = models.TextField(blank=False, )
    timestamp = models.DateTimeField(auto_now_add=True)


class Work(models.Model):
    GENRE_CHOICES = (
        ('novel', 'Novel'),
        ('poetry', 'Poetry'),
        ('sci_fi', 'Science Fiction'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('thriller', 'Thriller'),
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('auto_biography', 'Auto-Biography'),
        ('mystery', 'Mystery'),
        ('tragedy', 'Tragedy'),
        ('fantasy', 'Fantasy'),
        ('fairy_tale', 'Fairy Tale'),
        ('kids', 'children stories'),
        ('graphic_novel', 'Graphic Novel'),
        ('philosophy', 'Philosophy'),
        ('myth', 'Mythology'),
        ('comedy', 'Comedy'),
        ('textbook', 'Textbook'),
        ('encyclopedia', 'Encyclopedia'),
        ('academic_journal', 'Academic Journal'),
    )

    work_title = models.CharField(max_length=50, blank=True)
    author = models.CharField(max_length=100, blank=True, null=True,)
    uploader = models.ForeignKey(User, blank='True', related_name='work_user', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, )
    timestamp = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='novel')
    thumbnail = models.ImageField(upload_to=content_thumbnail_name, default='', blank='True', null=True, )
    file = models.FileField(upload_to=content_file_name, blank=True, null=True)

    class Meta:
        ordering = ('-timestamp',)
        indexes = (models.Index(fields=["work_title"]),)

    def __str__(self):
        return "{}".format(self.work_title)

class ReadingList(models.Model):
    r_list_name = models.CharField(max_length=50, )
    related_user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Work, blank=True, verbose_name="books",)

    class Meta:
        indexes = (models.Index(fields=["r_list_name", "related_user"]),)
        unique_together = (("r_list_name", "related_user"),)