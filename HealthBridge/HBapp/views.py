from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from urllib.parse import quote
from accounts.models import MyUser, Tag
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tags = MyUser.objects.get(user=request.user).tags
    return render(request, "index.html", {"tags": tags})


from django.conf import settings
from django.shortcuts import render
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import requests


def text_extraction(request):
    user = MyUser.objects.get(user=request.user)

    if request.method == "POST":
        # 이미지 파일을 사용자로부터 받아옴
        image_file = request.FILES["image"]

        # 이미지 파일을 임시로 저장할 경로 (인코딩 처리)
        image_path = os.path.join(settings.MEDIA_ROOT, quote(image_file.name))

        # 이미지 파일을 임시로 저장
        with open(image_path, "wb") as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        # Vision API 클라이언트 생성
        client = vision_v1.ImageAnnotatorClient()

        # 이미지를 바이너리로 읽어옴
        with open(image_path, "rb") as f:
            content = f.read()

        # 이미지 바이너리로부터 Vision API에서 처리할 이미지 객체 생성
        image = vision_v1.Image(content=content)

        # 텍스트 감지 수행
        response = client.text_detection(image=image)
        update_tags = {}
        # 텍스트 추출 결과
        extracted_text = ""
        for text_annotation in response.text_annotations:
            tags = Tag.objects.all()
            for t in tags:
                if text_annotation.description == t.name:
                    # tag, created = Tag.objects.update_or_create(name=text_annotation.description, slug=text_annotation.description)
                    user = MyUser.objects.get(user=request.user)
                    user.tags.add(t)
                    update_tags[t.pk] = t.name
                    user.save()
            extracted_text += text_annotation.description + "\n"

        # 이미지 파일을 삭제 (임시로 저장한 이미지를 사용하지 않을 경우)
        os.remove(image_path)

        return render(
            request,
            "result.html",
            {
                "response": response,
                "extracted_text": extracted_text,
                "update_tags": update_tags,
                "user": user,
            },
        )

    return render(request, "upload.html")


@login_required
def keyword_add(request):
    user = request.user
    my_user = MyUser.objects.get(user=request.user)
    user_tags = my_user.tags.all()
    all_tags = Tag.objects.all()
    if request.method == "POST":
        addTag = request.POST.getlist("addTag")
        my_user.tags.set(addTag)
        return redirect("HBapp:index")
    return render(
        request,
        "add.html",
        {
            "user_tags": user_tags,
            "all_tags": all_tags,
        },
    )
