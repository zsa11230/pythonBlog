from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def register():
    return None


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)  # 只是验证功能，还没有登录
        if user:
            print(user)  # username
            login(request, user)  # 验证通过，登录
            # 内部有request.user=user     可以用模板{{request.user}}
            # return redirect(request.GET.get("next", '/crm'))  # http://127.0.0.1:8080/login?next=/crm
            # 登录成功默认跳转用户信息页面，如果是其他页面来的，登录后跳转到其他页面
            return render(request, 'login.html')
        else:
            print(user)  # None
            print(type(user))  # <class 'NoneType'>
            error_msg = "用户名或密码错误"
            return render(request, "login.html", {"error_msg": error_msg})


def login_html(request):
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/login')
