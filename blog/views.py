from .models import Article, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'


class SingleView(DetailView):
    model = Article
    template_name = 'blog/single.html'
    context_object_name = 'post'


def singleArticle(request, id):
    data = get_object_or_404(Article, id=id)

    commentForm = CommentForm(request.POST)

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


class EditView(UpdateView):
    model = Article
    template_name = 'blog/edit.html'
    fields = '__all__'
    pk_url_kwargs = 'pk'
    success_url = reverse_lazy('blog:admin')


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
