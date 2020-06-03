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
from comment import views

urlpatterns = [
    # 新增文章评论
    path('create_comment', views.create_article_comment),
    # 新增评论的子评论
    path('create_child_comment', views.create_comment_child),
    # 获取文章评论
    path('article/<int:article_id>', views.get_article_comment),
]
