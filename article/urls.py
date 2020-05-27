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
from article import views

urlpatterns = [
    # 首页
    path('index', views.index),
    # 文章详情页
    path('detail/<int:article_id>', views.article_detail),
    # 文章新增页
    path('create', views.article_create_html),
    # 文章新增页
    path('create_request', views.article_create_request),
    # 首页加载更多文章ajax
    path('more', views.article_more),
    # 文章删除接口
    path('delete/<int:article_id>', views.article_delete_request),
]
