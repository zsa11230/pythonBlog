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
from django.contrib import admin
from django.urls import path
from article import views as article_views
from user import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', article_views.index),
    path('article/detail/<int:article_id>', article_views.article_detail),
    # 无路由情况下跳转到首页
    url(r'^$', article_views.index),
    path('login',user_views.login_html),
    path('login_request',user_views.login),
]
