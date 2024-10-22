from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.models import User
from article import models
from django.core.paginator import Paginator


# 用户登录，若账号不存在则直接注册并登录
def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        exist_flag = User.objects.filter(username=username).count()
        if exist_flag > 0:
            user = authenticate(username=username, password=password)  # 只是验证功能，还没有登录
            if user:
                login(request, user)  # 验证通过，登录
                return redirect('/')
            else:
                print(user)  # None
                print(type(user))  # <class 'NoneType'>
                error_msg = "用户名或密码错误"
                return render(request, "login.html", {"error_msg": error_msg})
        else:
            # 若用户名不存在则直接注册新用户
            new_user = User.objects.create_user(username=username, password=password)
            login(request, new_user)
            return redirect('/')


# 登录页面
def login_html(request):
    return render(request, 'login.html')


# 登出
def user_logout(request):
    logout(request)
    return redirect('/')


# 后台管理页面
def backstage_manage(request):
    manage_flag = request.user.is_superuser
    if manage_flag:
        return render(request, 'backstage/manage_index.html')
    else:
        return redirect('/')


# 后台文章管理页面
def backstage_article_manage(request):
    manage_flag = request.user.is_superuser
    if manage_flag:
        size = request.GET.get('size')
        current = request.GET.get('current')
        blog_index = models.Article.objects.filter(del_flag=False).all().order_by('-id')
        if current is None:
            current = 1
        else:
            int(current)
        if size is None:
            size = 10
        else:
            int(size)
        paginator = Paginator(blog_index, size)
        page = paginator.page(current)
        context = {"page": page}
        return render(request, 'backstage/manage_article.html', context)
    else:
        return redirect('/')