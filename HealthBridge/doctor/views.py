from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Doctor, Hospital
from django.contrib.auth.models import User

# Create your models here.

# Create your views here.


def doctor_signup(request):
    hospitals = Hospital.objects.all()  # 모든 병원 정보를 가져옴
    if request.method == "POST":
        username = request.POST["username"]  # 아이디
        password = request.POST["password"]  # 비밀번호
        password2 = request.POST["password2"]  # 비밀번호 확인
        license_number = request.POST["license_number"]  # 면허번호
        # hospital_id = request.POST['hospital']
        full_name = request.POST["fullname"]  # 이름
        hospital_id = request.POST["hospital"]  # 병원

        first_name, last_name = full_name.split()

        hospital = Hospital.objects.get(id=hospital_id)
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
        )
        doctor = Doctor(
            doctor_user=user, license_number=license_number, hospital=hospital
        )

        doctor.save()

        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("HBapp:index")

    return render(request, "doctor_signup.html", {"hospitals": hospitals})


# def select_hospital(request):
#     hospitals = Hospital.objects.all()
#     return render(request, 'select_hospital.html', {'hospitals': hospitals})


def dropdown_view(request):
    hospitals = Hospital.objects.all()  # 모든 병원 정보를 가져옴
    return render(request, "select_hospital.html", {"hospitals": hospitals})
