from django.views.generic.detail import DetailView
from .models import Article
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'


class SingleView(DetailView):
    model = Article
    template_name = 'blog/single.html'
    context_object_name = 'post'


class AdminView(ListView):
    model = Article
    template_name = 'blog/admin.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Article
    fields = ['name']
    template_name = 'blog/add.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:admin')
