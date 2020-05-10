from django.shortcuts import render
from article import models


def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    tags = models.Tags.objects.order_by('-id')[0:10]
    context = {
        'articles': blog_index,  # 文章数据
        'tags': tags,  # 标签
    }
    return render(request, 'index.html', context)
