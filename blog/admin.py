from django.contrib import admin
from .models import Comment, Article, Reply

admin.site.register(Comment)
admin.site.register(Article)
admin.site.register(Reply)
