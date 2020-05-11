from django.shortcuts import render
from article import models


def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    tags = models.Tags.objects.order_by('-id')[0:10]
    images = []
    for art in blog_index:
        if len(art.image_url) != 0:
            if len(images) < 5:
                img = models.Article()
                img.image_url = art.image_url
                img.title = art.title
                img.id = art.id
                images.append(img)
            else:
                break
    context = {
        'articles': blog_index,  # 文章数据
        'tags': tags,  # 标签
        'images': images,  # 轮播图
    }
    return render(request, 'index.html', context)
