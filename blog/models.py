from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    img = models.FileField(
        upload_to='media', default='../static/blog/logo.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author.username

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=CASCADE)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
