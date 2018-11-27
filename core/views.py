from django.shortcuts import render
from core.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {
        'post': post,
    })

    