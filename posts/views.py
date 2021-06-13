from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from yatube2.settings import POSTS_IN_PAGINATOR
from .models import Post, Group

User = get_user_model()


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'posts/index.html',
        {'page': page}
    )


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.filter(group=group).order_by("-pub_date")
    paginator = Paginator(posts, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "group": group,
        "page": page
    }

    return render(request, "posts/group.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all().order_by("-pub_date")
    paginator = Paginator(posts, POSTS_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'author': author,
        "posts_count": author.posts.count()
    }

    return render(request, 'posts/profile.html', context)


def post_view(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, id=post_id)
    author = post.author
    posts_count = author.posts.count()

    context = {
        "post": post,
        "author": author,
        "posts_count": posts_count,
    }

    return render(request, 'posts/post.html', context)
