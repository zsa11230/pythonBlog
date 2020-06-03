"""pythonBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from common import views

urlpatterns = [
    # 登录页面
    path('login',views.login_html),
    # 登出
    path('logout',views.user_logout, name="logout"),
    # 登录
    path('login_request',views.user_login),
    # 后台管理页面
    path('backstage/manage',views.backstage_manage),
    # 后台文章管理页面
    path("backstage/manage/article", views.backstage_article_manage),
]
