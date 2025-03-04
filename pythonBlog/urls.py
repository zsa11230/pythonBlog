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
from article import views as article_views, urls as article_urls
from django.conf.urls import url, include
from common import urls as user_urls
from comment import urls as comment_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # 无路由情况下跳转到首页
    url(r'^$', article_views.index),
    # 引入用户部分路由
    url(r'user/', include(user_urls)),
    # 引入文章部分路由
    url(r'article/', include(article_urls)),
    # 引入评论部分路由
    url(r'comment/', include(comment_urls)),
]
