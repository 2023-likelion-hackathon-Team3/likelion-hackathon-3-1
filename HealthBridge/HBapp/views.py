from django.shortcuts import render
import os
from urllib.parse import quote
from accounts.models import MyUser, Tag
# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.conf import settings
from django.shortcuts import render
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

def text_extraction(request):
    if request.method == 'POST':
        # 이미지 파일을 사용자로부터 받아옴
        image_file = request.FILES['image']

        # 이미지 파일을 임시로 저장할 경로 (인코딩 처리)
        image_path = os.path.join(settings.MEDIA_ROOT, quote(image_file.name))

        # 이미지 파일을 임시로 저장
        with open(image_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        # Vision API 클라이언트 생성
        client = vision_v1.ImageAnnotatorClient()

        # 이미지를 바이너리로 읽어옴
        with open(image_path, 'rb') as f:
            content = f.read()

        # 이미지 바이너리로부터 Vision API에서 처리할 이미지 객체 생성
        image = vision_v1.Image(content=content)

        # 텍스트 감지 수행
        response = client.text_detection(image=image)

        # 텍스트 추출 결과
        extracted_text = ""

        for text_annotation in response.text_annotations:
            if text_annotation.description == "시력":
                tag, created = Tag.objects.update_or_create(name=text_annotation.description, slug=text_annotation.description)
                user = MyUser.objects.get(user=request.user)
                update_tags = user.tags.add(tag)
                user.save()
            extracted_text += text_annotation.description + "\n"

        # 이미지 파일을 삭제 (임시로 저장한 이미지를 사용하지 않을 경우)
        os.remove(image_path)

        return render(request, 'result.html', {'response':response, 'extracted_text': extracted_text})

    return render(request, 'upload.html')