from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from core.forms import PostForm, CommentForm
from core.models import Post, Comment


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


@login_required
def edit_post(request, slug):
    """
    user can edit posts with form - consider changing for admin use only
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


def create_post(request):
    """user can create a post"""
    form_class = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('index.html')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {
        'form': form,
    })


def create_comment(request, slug):
    """user can create comments on existing posts"""
    post = Post.objects.get(slug=slug)
    form_class = CommentForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {
        'post': post,
        'form': form,
    })
