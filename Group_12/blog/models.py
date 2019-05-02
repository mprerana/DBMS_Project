from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class interest(models.Model):
    interest_name = models.TextField()
    content = models.TextField(null=True)
    base_image = models.ImageField(upload_to='media/interest/', null=True, blank=True)
    related_topics = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return str(self.interest_name)

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(name__lte=self.interest_name)


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cover_photo =  models.TextField(null=True,blank=True)
    heading = models.CharField(max_length=200)
    content = RichTextUploadingField()
    draft = models.BooleanField(default=False)
    post_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    interests = models.ForeignKey(interest, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("blog:show_blog", kwargs={"blog_id": self.pk})

    def get_upvote_url(self):
        return reverse("blog:like", kwargs={"blog_id": self.pk})

    def get_upvote_api_url(self):
        return reverse("blog:api_like", kwargs={"blog_id": self.pk})


# class upvote(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
#     blog=models.ForeignKey(Blog, on_delete=models.CASCADE,null=True,blank=True)
#     created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def children(self):
        return Comment.objects.filter(parent=self)

class Deleted_Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cover_photo = models.TextField(null=True, blank=True)
    heading = models.CharField(max_length=200)
    content = RichTextUploadingField()
    post_date = models.DateTimeField(auto_now_add=True)
    interests = models.ForeignKey(interest, blank=True, on_delete=models.CASCADE)
    delete_date = models.DateField(auto_now_add=True)

