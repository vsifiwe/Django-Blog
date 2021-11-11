from django.http import request
from .models import Article, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm, CreateUserForm, ArticleForm
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


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blog/confirm-delete.html'
    pk_url_kwargs = 'pk'
    success_url = reverse_lazy('blog:admin')


class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)


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
