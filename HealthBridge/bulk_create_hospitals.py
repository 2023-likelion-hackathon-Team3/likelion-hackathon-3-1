import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthBridge.settings")
django.setup()

from doctor.models import Hospital

csv_path = "C:/LEEKYUMIN/likelion/2023 hackathon/likelion-hackathon-3/HealthBridge/hospital.csv"  # 본인의 CSV 파일 경로로 수정해주세요

with open(csv_path, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile)
    hospitals = []
    for row in csvreader:
        hospital = Hospital(
            hospital_name=row["name"],
            address=row["address"],
            telephone=row["telephone"],
        )
        hospitals.append(hospital)
    Hospital.objects.bulk_create(hospitals)

print("Hospitals added successfully.")
