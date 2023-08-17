from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Doctor, Hospital, DoctorAnswer
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from board.models import *
from django.http import HttpResponseRedirect
from accounts.models import MyUser

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

        hospital = Hospital.objects.get(id=hospital_id)
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=full_name,
            is_staff=True,
        )
        doctor = Doctor(
            doctor_user=user, license_number=license_number, hospital=hospital
        )

        doctor.save()

        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("doctor:doctor_main")

    return render(request, "doctor_signup.html", {"hospitals": hospitals})


# def select_hospital(request):
#     hospitals = Hospital.objects.all()
#     return render(request, 'select_hospital.html', {'hospitals': hospitals})


def dropdown_view(request):
    hospitals = Hospital.objects.all()  # 모든 병원 정보를 가져옴
    return render(request, "select_hospital.html", {"hospitals": hospitals})


def doctor_login(request):
    if request.method == "POST":
        userid = request.POST["username"]
        pwd = request.POST["password"]
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("doctor:doctor_main")
        else:
            return render(request, "doctor_login.html")
    else:
        return render(request, "doctor_login.html")


def doctor_main(request):
    question_list = Board.objects.all().order_by("-pk")
    return render(request, "doctor_main.html", {"question_list": question_list})


def doctor_result(request, id):
    list = get_object_or_404(Board, pk=id)
    answer = DoctorAnswer.objects.filter(board_list=list)

    if request.method == "POST":
        new_answer = DoctorAnswer()
        doctor = Doctor.objects.get(doctor_user=request.user)
        new_answer.doctor = doctor
        new_answer.answer = request.POST.get("doctor_answer")
        new_answer.board_list = list
        list.answer = True
        list.save()
        new_answer.save()

        return redirect("doctor:doctor_main")

    try:
        answer = DoctorAnswer.objects.filter(board_list=list)
    except DoctorAnswer.DoesNotExist:
        answer = None

    return render(request, "doctor_result.html", {"list": list, "answer": answer})


def map_view(request, id):
    context = {"GOOGLE_MAPS_API_KEY": "AIzaSyAkJA2jmINMwar5RtFJlGV9bCVm8P4tM3Q"}
    doctor = Doctor.objects.get(pk=id)
    myuser = MyUser.objects.get(pk=id)
    address = doctor.hospital.address
    hospital_name = doctor.hospital.hospital_name

    if request.method == "POST":
        doctor.introduction = request.POST.get("introduction")
        doctor.history = request.POST.get("history")
        doctor.save()
        return redirect("doctor:doctor-info", id)

    return render(
        request,
        "doctor_info.html",
        {
            "context": context,
            "address": address,
            "hospital_name": hospital_name,
            "doctor": doctor,
            "myuser": myuser,
        },
    )


def doctor(request):
    return render(request, "doctor_start.html")
