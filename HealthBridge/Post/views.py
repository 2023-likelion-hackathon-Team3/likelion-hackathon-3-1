from django.shortcuts import render, redirect
from .models import Post, Tag
from accounts.models import MyUser, User
from django.urls import reverse


def postList(request):
    posts = Post.objects.all().order_by('-pk')
    tags = Tag.objects.all()
    user = request.user

    if user.is_authenticated and MyUser.objects.get(user=user).tags.exists():
        user_tags = MyUser.objects.get(user=user).tags
        posts = posts.filter(tags__in=user_tags.iterator()).distinct()
        print(posts)
    else:
        user_tags = tags

    return render(request, 'postList.html', {'posts' : posts, 'tags':tags, 'user_tags':user_tags})

def postDetail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'postDetail.html', {'post':post})


def postUpdate(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        post.save()

        return redirect("post:postDetail", post.pk)
    return render(request, "postUpdate.html", {'post':post})


def postDelete(request, pk):
    post = Post.objects.get(pk=pk)

    post.delete()
    return redirect("post:postList")

def tag_page(request, slug):
    tags = Tag.objects.all()
    tag = Tag.objects.get(slug=slug)
    posts = tag.post_set.all().order_by('-pk')
    user = request.user
    
    if MyUser.objects.get(user=user).tags == None:
        user_tags == tags
    else :
        user_tags = MyUser.objects.get(user=user).tags

    return render(request, 'tag.html', {'posts':posts, 'tag':tag , 'tags':tags, 'user_tags':user_tags})