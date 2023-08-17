from django.shortcuts import render

import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import base64


def webcam_view(request):
    return render(request, "camera.html")


def save_cropped_photo(request):
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        cropped_photo_data = request.POST.get("cropped_photo_data", None)

        if cropped_photo_data:
            # Decode base64 image data
            _, encoded = cropped_photo_data.split(",", 1)
            image_data = encoded.encode("utf-8")

            # Create a filename for the new image
            filename = os.path.join(settings.MEDIA_ROOT, "cropped_photo.jpg")

            # Save the image to the media directory
            with open(filename, "wb") as f:
                f.write(base64.b64decode(image_data))

            return JsonResponse(
                {"success": True, "message": "Cropped photo saved successfully."}
            )
        else:
            return JsonResponse(
                {"success": False, "message": "No image data provided."}
            )

    return JsonResponse({"success": False, "message": "Invalid request."})


def crop(request):
    return render(request, "camera_crop.html")


def save_webcam_photo(request):
    if request.method == "GET":
        return render(request, "webcam.html")
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        cropped_photo_data = request.POST.get("capturedDataUrl", None)

        if cropped_photo_data:
            # Decode base64 image data
            _, encoded = cropped_photo_data.split(",", 1)
            image_data = encoded.encode("utf-8")

            # Create a filename for the new image
            filename = os.path.join(settings.MEDIA_ROOT, "captured_photo.jpg")

            # Save the image to the media directory
            with open(filename, "wb") as f:
                f.write(base64.b64decode(image_data))

            return JsonResponse(
                {"success": True, "message": "Cropped photo saved successfully."}
            )
        else:
            return JsonResponse(
                {"success": False, "message": "No image data provided."}
            )

    return JsonResponse({"success": False, "message": "Invalid request."})


def webcam_capture_view(request):
    if request.method == "GET":
        return render(request, "cameraonly.html")
    response_data = {
        "success": True,
        "redirect_url": "/camera/captured_image/",  # 리다이렉트하고자 하는 URL로 변경
    }
    return JsonResponse(response_data)


def captured_image_crop_view(request):
    captured_data_url = request.GET.get("captured_data_url", "")
    context = {"captured_data_url": captured_data_url}
    return render(request, "captured_image_crop.html", context)


from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from accounts.models import MyUser
from Post.models import Tag
from urllib.parse import quote


def text_extraction(request):
    user = MyUser.objects.get(user=request.user)

    if request.method == "GET":
        # # 이미지 파일을 사용자로부터 받아옴
        # image_file = request.FILES["image"]

        # # 이미지 파일을 임시로 저장할 경로 (인코딩 처리)
        # image_path = os.path.join(settings.MEDIA_ROOT, quote(image_file.name))

        # # 이미지 파일을 임시로 저장
        # with open(image_path, "wb") as f:
        #     for chunk in image_file.chunks():
        #         f.write(chunk)

        image_path = "media/cropped_photo.jpg"

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


def text_extraction1(request):
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

        image_path = "media/cropped_photo.png"

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

        return render(
            request,
            "result1.html",
            {
                "response": response,
                "extracted_text": extracted_text,
                "update_tags": update_tags,
                "user": user,
            },
        )
    return render(request, "upload.html")
