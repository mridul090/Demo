from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User,default=None)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20]+"..."

class Comment(models.Model):
    message = models.TextField('Message')
    user_name = models.CharField(max_length=255,blank=True)
    date_comment = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(Article,default=None)
