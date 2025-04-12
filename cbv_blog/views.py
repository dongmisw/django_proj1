

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cbv_blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = 'pk'
    #template_name = 'cbv_blog/index.html'

class PostDetail(DetailView):
    model = Post