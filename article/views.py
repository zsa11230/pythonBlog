from django.shortcuts import render
from article import models


def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'articles': blog_index,  # 将数据保存在blog_index
    }
    return render(request, 'index.html', context)
