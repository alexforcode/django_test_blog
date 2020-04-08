from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 3
    queryset = Post.published.all()
    template_name = 'blog/post/list.html'


class PostDetailView(DetailView):
    context_object_name = 'post'
    queryset = Post.published.all()
    template_name = 'blog/post/detail.html'
