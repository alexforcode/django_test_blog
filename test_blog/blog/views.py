from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'
