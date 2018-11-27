from django.shortcuts import render, redirect
from core.forms import PostForm
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

def edit_post(request, slug):
    """
    user can edit links with form 
    """
    post = Post.objects.get(slug=slug)
    form_class = PostForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class(instance=post)
    return render(request, 'posts/edit_post.html', {
            'post': post,
            'form': form,
    })