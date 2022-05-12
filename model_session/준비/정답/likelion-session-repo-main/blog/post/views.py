from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def mypage(request):
    posts = Post.objects.all() #모든 post 다 불러오기
    post_list = posts.filter(user=request.user)  # 내가 쓴글만

    return render(request, 'mypage.html',{"post_list":post_list})


def writing(request):
    if request.method == "GET":
        return render(request, 'writing.html')

    elif request.method == "POST":
        post = Post()
        post.user = request.user
        post.content = request.POST["content"]
        post.save()
        return redirect('/')
    return render(request, 'writing.html')


def main(request):

    return render(request, 'main.html')
