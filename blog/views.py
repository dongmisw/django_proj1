from django.shortcuts import render

from blog.models import Post


# Create your views here.

def index(request):
    return render(
        request,
        'blog/index.html',
        {
            'posts': Post.objects.all().order_by('-pk'),
        }
    )
