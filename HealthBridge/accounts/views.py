from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == "POST":
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('HBapp:index')
        else:
            return render(request, 'login.html', {'error': '입력한 내용을 다시 확인해주세요.'})
    else: 
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=userid).exists():
            return render(request, 'signup.html', {'error': '이미 존재하는 아이디입니다.'})

        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['userid'], password=request.POST['password'])
            
            user = authenticate(request, username=userid, password=password, backend='django.contrib.auth.backends.ModelBackend')
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)
                return render(request, 'login.html')
            else:
                # 사용자 인증에 실패한 경우에 대한 처리
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
        
    return render(request, 'signup.html')

@login_required
def set_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        request.user.set_password(new_password)
        request.user.save()

        # 세션 인증 업데이트
        update_session_auth_hash(request, request.user)

        return redirect('HBapp:index')  # 로그인 후 리다이렉트할 페이지
    return render(request, 'set_password.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

def start(request):
    return render(request, 'start.html')