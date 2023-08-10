from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Doctor, Hospital
from django.contrib.auth.models import User

# Create your views here.

def doctor_signup(request):
    if request.method == 'POST':
        username = request.POST['username'] #아이디
        password = request.POST['password'] #비밀번호
        password2 = request.POST['password2'] #비밀번호 확인
        license_number = request.POST['license_number'] #면허번호
        #hospital_id = request.POST['hospital']
        full_name = request.POST['full_name'] #이름
        
        first_name, last_name = full_name.split()
        
        #hospital = Hospital.objects.get(id=hospital_id)
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        doctor = Doctor(user=user, license_number=license_number)
        doctor.save()
        
        login(request, user)
        return redirect('HBapp:index')

    return render(request, 'doctor_signup.html')

def select_hospital(request):
    hospitals = Hospital.objects.all()
    return render(request, 'select_hospital.html', {'hospitals': hospitals})