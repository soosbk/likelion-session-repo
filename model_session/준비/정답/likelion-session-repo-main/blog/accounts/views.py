from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Profile
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':  # 값이 넘겨졌을 경우
        if request.POST['password1'] == request.POST['password2']:  # password 1,2입력된 값이 같다면
            
            user = User.objects.create_user(  # user 객체를 생성
                username=request.POST["username"],
                password=request.POST["password1"])

            profile = Profile()  # profile 객체를  생성
            profile.user = user
            profile.nickname = request.POST["nickname"]
            
            profile.save()
            return render(request,'main.html')  # 첫화면으로
    return render(request, 'signup.html')

