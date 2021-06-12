from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Group


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "posts/index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.filter(group=group).order_by("-pub_date")[:12]
    # posts = group.posts.all()

    context = {
        "group": group,
        "page": posts
    }

    return render(request, "posts/group.html", context)
