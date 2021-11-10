from django.db import models
from django.db.models.deletion import CASCADE


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    # Add an image field

    def __str__(self):
        return self.title + ' by ' + self.author

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=CASCADE)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
