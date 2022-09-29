from django.shortcuts import render
from .models import Posts, Tag
from django.views.generic import DetailView, ListView

class PostDetailView(DetailView):
    model = Posts
    context_object_name = "posts"
    slug_url_kwarg = 'posts_slug'
    template_name = 'blog/post_detail.html'

class PostListView(ListView):
    model = Posts
    paginate_by = 9
    template_name = "blog/posts_list.html"
