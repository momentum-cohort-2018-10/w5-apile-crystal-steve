from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count
from core.forms import PostForm, CommentForm
from core.models import Post, Comment, Vote
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {
        'post': post,
    })

# def listing(request):
#     post_list = Posts.objects.all()
#     paginator = Paginator(post_list, 3)

#     page = request.GET.get('page')
#     posts = paginator.get_page(page)
#     return render(request, 'index.html', {'posts': posts})

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
            success_msg = f"Your edits have been incorporated successfully.  Thanks."
            messages.add_message(request, messages.SUCCESS, success_msg)
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
            success_msg = f"Your post has been created!  Thanks."
            messages.add_message(request, messages.SUCCESS, success_msg)
            return redirect('home')
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
            comment.commenter = request.user
            comment.post = post
            comment.save()
            success_msg = f"Thanks for sharing your opinion."
            messages.add_message(request, messages.SUCCESS, success_msg)
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {
        'post': post,
        'form': form,
    })


def upvote_list(request):
    posts = request.user.vote_set_posts.all()
    return render_post_list(request, 'my up voted posts', posts)

@require_POST
def voting(request, slug):
    if request.method == "POST":
        post = Post.objects.get(slug=slug)
        if post in request.user.upvote_list.all():
            post.vote_set.get(user = request.user).delete()
            messages.add_message(request,messages.INFO,"WTF Dude!")

        else:
            post.vote_set.create(user=request.user)
            messages.add_message(request,messages.INFO,"WOW, Thanks Man!")
    return redirect(f'/#post-{post.slug}')

def test_vote(request):
    post = Post.objects.first()
    voter = User.objects.first()
    vote = Vote.objects.create(post = post, voter = voter)
    context = {'vote': vote}
    return render(request, 'test/test_vote.html')


# def vo(request, slug):
#     """
#     gets the post that will be voted on 
#     """
#     post = Post.objects.get(slug=slug)
#     if post in request.voter.vote_set.all():
#         post.vote_set.get(user=request.user).delete()
#         #message = f"you have taken back your vote"
#     else:
#         post.vote_set.create(user=request.user)
#         message = f"you have just  up voted {post.title}."

#         messages.add_message(request, messages.INFO, message)
#         return redirect(f'/#post-{post.slug}')
#         return render('thanks dude')