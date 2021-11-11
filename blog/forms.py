from django import forms
from django.forms import ModelForm
from .models import Article, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'img']
