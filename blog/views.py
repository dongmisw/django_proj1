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
def single_post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,
                  'blog/single_post_page.html',
                  {'post': post}
                  )
