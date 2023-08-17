import os
import csv

# Django 설정 초기화
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "HealthBridge.settings"
)  # 'your_project.settings'는 실제 프로젝트의 settings 모듈 경로로 변경

import django

django.setup()

from Post.models import Tag

# CSV 파일 경로
csv_file_path = (
    "C:/LEEKYUMIN/likelion/2023 hackathon/likelion-hackathon-3/HealthBridge/keyword.csv"
)

# CSV 파일 읽기
with open(csv_file_path, "r", encoding="CP949") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        name = row["name"]
        slug = row["slug"]
        tag, created = Tag.objects.get_or_create(name=name, slug=slug)
        if created:
            print(f"Tag '{name}' created.")
        else:
            print(f"Tag '{name}' already exists.")

print("Import finished.")
