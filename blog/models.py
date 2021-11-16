from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


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
    author = models.ForeignKey(User, on_delete=CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=CASCADE)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=CASCADE)
    reply = models.CharField(max_length=100)

    def __str__(self):
        return self.reply
