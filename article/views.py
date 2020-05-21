from django.shortcuts import render
from article import models
from django.core.paginator import Paginator


def index(request):
    # 获取文章列表
    blog_images = models.Article.objects.all().order_by('hits')
    tags = models.Tags.objects.order_by('-id')[0:20]
    images = []
    for art in blog_images:
        if len(art.image_url) != 0:
            if len(images) < 5:
                img = models.Article()
                img.image_url = art.image_url
                img.title = art.title
                img.id = art.id
                images.append(img)
            else:
                break

    size = request.GET.get('size')
    current = request.GET.get('current')
    blog_index = models.Article.objects.all().order_by('-id')
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
    context = {
        'tags': tags,  # 标签
        'images': images,  # 轮播图
        "page": page,  # 文章数据
    }
    return render(request, 'index.html', context)


# 文章详情页面
def article_detail(request, article_id):
    blog = models.Article.objects.get(id=article_id)
    # 每访问一次增加一点击量
    blog.hits = blog.hits + 1
    blog.save()
    context = {
        'blog': blog,  # 文章内容数据
    }
    return render(request, 'article_detail.html', context)
