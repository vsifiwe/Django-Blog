from django.http import request
from .models import Article, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm, CreateUserForm, ArticleForm, ReplyForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index_View(request):
    data = Article.objects.all()
    context = {
        'data': data
    }

    return render(request, 'blog/index.html', context)


def singleArticle(request, id):
    data = get_object_or_404(Article, id=id)

    commentForm = CommentForm()

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            post = commentForm.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            
            post.article = data
            post.save()
            commentForm = CommentForm()
    context = {
        'post': data,
        'forms': commentForm
    }
    return render(request, 'blog/single.html', context)


@login_required(login_url='blog:login')
def Admin_View(request):
    post_list = Article.objects.all()
    context = {
        'post_list': post_list
    }

    return render(request, 'blog/admin.html', context)


def createArticle(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog:admin')

    context = {
        'form': form
    }

    return render(request, 'blog/add.html', context)


def updateArticle(request, pk):
    data = get_object_or_404(Article, id=pk)
    form = ArticleForm(instance=data)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=data)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog:admin')

    context = {
        'form': form
    }

    return render(request, 'blog/edit.html', context)


def deleteArticle(request, pk):

    article = get_object_or_404(Article, id=pk)

    if request.method == 'POST':

        if request.user == article.author:
            article.delete()
            return redirect('blog:admin')
        else:
            messages.info(request, 'You are not allowed to delete this post')

    context = {
        'article': article
    }

    return render(request, 'blog/confirm-delete.html', context)


def viewReplies(request, pk):
    replyForm = ReplyForm()
    comment = get_object_or_404(Comment, id=pk)

    if request.method == 'POST':
        replyForm = ReplyForm(request.POST)

        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            if request.user.is_authenticated:
                reply.author = request.user
            reply.comment = comment
            reply.save()
            replyForm = ReplyForm()
            # return redirect('blog:comment', pk=pk)

    data = comment.reply_set.all

    context = {
        'data': data,
        'form': replyForm
    }

    return render(request, 'blog/reply.html', context)


def User_Register(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog:login')

    context = {
        'form': form
    }

    return render(request, 'blog/register.html', context)


def Login_User(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog:index')
        else:
            messages.info(request, 'Username or Password do not exist')

    return render(request, 'blog/login.html')


def Logout_User(request):

    logout(request)
    return redirect('blog:index')
