from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from accounts.models import MyUser
from board.models import Board
from Post.models import Tag

# Create your views here.

@login_required
def my(request):
    if request.user.is_authenticated:
        tags = MyUser.objects.get(user=request.user).tags
    else:
        tags=None #로그인 하지 않았을 경우
    now_user = request.user
    myuser = MyUser.objects.get(user=request.user)
    user_questions = Board.objects.filter(hb_user=now_user)
    return render(
        request,
        "my.html",
        {"tags": tags, "questions": user_questions, "myuser": myuser},
    )


@login_required
def check(request):
    if request.method == "POST":
        password = request.POST.get("password")

        user = authenticate(request, username=request.user.username, password=password)

        if user is not None:
            return render(request, "fix.html", {"user": user})
        return render(request, "check.html")
    return render(request, "check.html")


@login_required
def fix(request):
    if request.method == "POST":
        myuser = MyUser.objects.get(user=request.user)
        try:
            image = request.FILES["image"]
        except:
            if myuser.image == None:
                image = None
            else:
                image = myuser.image
        new_username = request.POST.get("new_username")
        if new_username == None:
            new_username = request.user.username
        new_password = request.POST.get("new_password")
        new_password2 = request.POST.get("new_password2")

        myuser.image = image
        myuser.save()

        if (
            User.objects.filter(username=new_username).exists()
            and new_username != request.user.username
        ):
            error_message = "이미 사용 중인 아이디입니다."
            return render(request, "fix.html", {"error_message": error_message})

        if new_password != new_password2:
            error_message = "비밀번호가 일치하지 않습니다."
            return render(request, "fix.html", {"error_message": error_message})

        request.user.username = new_username
        request.user.save()

        request.user.set_password(new_password)
        request.user.save()

        update_session_auth_hash(request, request.user)  # 세션 업데이트

        return redirect("mypage:my")
    return render(request, "fix.html", {"myuser": myuser})


def addTag(request):
    user = request.user
    my_user = MyUser.objects.get(user=request.user)
    user_tags = my_user.tags.all()
    all_tags = Tag.objects.all()
    if request.method == "POST":
        addTag = request.POST.getlist("addTag")
        my_user.tags.set(addTag)
        return redirect("mypage:my")
    return render(
        request, "add_tag.html", {"user_tags": user_tags, "all_tags": all_tags}
    )


# def deleteTag(request):
#     user = request.user
#     my_user = MyUser.objects.get(user=user)
#     user_tags = my_user.tags.all()
#     all_tags = Tag.objects.all()
#     if request.method == 'POST':
#         deleteTag = request.POST.getlist('deleteTag')
#         for tag_id in deleteTag:
#             tag = Tag.objects.get(id=tag_id)
#             my_user.tags.remove(tag)
#         return redirect('mypage:my')
#     return render(request, 'delete_tag.html', {'user_tags': user_tags, 'all_tags': all_tags})
