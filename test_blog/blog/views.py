from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import SharePostForm
from .models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 3
    queryset = Post.published.order_by('-publish')
    template_name = 'blog/post/list.html'


class PostDetailView(DetailView):
    context_object_name = 'post'
    queryset = Post.published.all()
    template_name = 'blog/post/detail.html'


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = SharePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} ({cd["email"]}) recommends you reading {post.title}'
            message = f'Read "{post.title}" at {post_url}\n\n{cd["name"]}\'s comments: {cd["comments"]}'

            send_mail(subject, message, 'admin@example.com', [cd['to']])
            sent = True
    else:
        form = SharePostForm()

    context = {'post': post, 'form': form, 'sent': sent}
    return render(request, 'blog/post/share.html', context)
