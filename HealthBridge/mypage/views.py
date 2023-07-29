from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.

def my(request):
    return render(request, 'my.html')

@login_required
def check(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        
        user = authenticate(request, username=request.user.username, password=password)
        
        if user is not None:
            return render(request, 'fix.html', {'user': user})
        return render(request, 'check.html')
    return render(request, 'check.html')

@login_required
def fix(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        new_password2 = request.POST.get('new_password2')
        
        if User.objects.filter(username=new_username).exists():
            error_message = "이미 사용 중인 아이디입니다."
            return render(request, 'fix.html', {'error_message': error_message})
        
        if new_password != new_password2:
            error_message = "비밀번호가 일치하지 않습니다."
            return render(request, 'fix.html', {'error_message': error_message})
        
        request.user.username = new_username
        request.user.save()
        
        request.user.set_password(new_password)
        request.user.save()
        
        update_session_auth_hash(request, request.user) #세션 업데이트
        
        return redirect('mypage:my')
    return render(request, 'fix.html')