from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']: # 입력한 두개의 비밀번화 맞는지
            try: # 입력한 아이디가 기존에 존재하는 아이디인지
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': '이미 사용중인 아이디 입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 다릅니다.'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 틀립니다.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST': 
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')

