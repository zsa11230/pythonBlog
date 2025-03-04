import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from article import models
from django.core.paginator import Paginator, EmptyPage
from article.models import Tags
from pythonBlog.SqlCustomQuery import custom_query


# 站点配置，首页导航栏
def site_config():
    sql_result = custom_query('SELECT tags_id, count(1) AS count FROM article_article_tags GROUP BY tags_id ORDER BY count DESC LIMIT 4')
    tag_ids = []
    for result in sql_result:
        tag_ids.append(result[0])
    tags = models.Tags.objects.filter(id__in=tag_ids)
    context = {
        'nav': tags,  # 导航标签
    }
    return context


# 首页
def index(request):
    # 加载站点配置
    context = site_config()
    # 获取文章列表
    blog_images = models.Article.objects.filter(del_flag=False).all().order_by('hits')
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
    blog_index = models.Article.objects.filter(del_flag=False).all().order_by('-id')[0:10]
    context['tags'] = tags  # 标签
    context['images'] = images  # 轮播图
    context['page'] = blog_index  # 文章数据
    return render(request, 'index.html', context)


# 加载更多ajax
def article_more(request):
    blog_index = models.Article.objects.filter(del_flag=False).all().order_by('-id')
    size = request.GET.get('size')
    current = request.GET.get('current')
    if current is None or current == '':
        current = 1
    else:
        int(current)
    if size is None or current == '':
        size = 10
    else:
        int(size)
    paginator = Paginator(blog_index, size)
    try:
        page = paginator.page(current)
    except EmptyPage:
        return HttpResponse(None)

    result = []
    for blog in page:
        tags = blog.tags.all()
        tags_result = []
        for tag in tags:
            tags_result.append(tag.name)
        context = {
            'image_url': blog.image_url,  # 预览图地址
            'id': blog.id,  # id
            'title': blog.title,  # 标题
            'intro': blog.intro,  # 标题
            'username': blog.user.username,  # 作者名
            'created_time': str(blog.created_time),  # 创建时间
            'hits': blog.hits,  # 点击数
            'tags': tags_result,  # 标签
        }
        result.append(context)

    return HttpResponse(json.dumps({
        "blog_index": result,
        "current": current,
        "size": size,
    }))


# 文章详情页面
def article_detail(request, article_id):
    # 加载站点配置
    context = site_config()
    blog = models.Article.objects.get(id=article_id)
    # 每访问一次增加一点击量
    blog.hits = blog.hits + 1
    blog.save()
    context['blog'] = blog  # 文章内容数据
    return render(request, 'article_detail.html', context)


# 文章新增页面
def article_create_html(request):
    # 加载站点配置
    context = site_config()
    # 如果用户未登录则跳登录页面
    user = request.user
    if user.username == '':
        return redirect('/user/login')
    categories = models.Category.objects.all().order_by('-id')
    context['categories'] = categories  # 分类
    return render(request, 'article_create.html', context)


# 文章新增请求
def article_create_request(request):
    # 如果用户未登录则跳登录页面
    user = request.user
    if user.username == '':
        return redirect('/user/login')
    title = request.POST.get("title")
    image_url = request.POST.get("image_url")
    intro = request.POST.get("intro")
    category_id = int(request.POST.get("category"))
    category = models.Category.objects.get(id=category_id)
    body = request.POST.get("body")
    new_article = models.Article.objects.create(title=title, image_url=image_url
                                                , intro=intro, category=category, body=body, user=user, hits=0)
    # 保存标签
    tags = request.POST.get("tags")
    tags_array = tags.replace("，", ",").replace(" ", ",").replace(";", ",").replace("；", ",").split(',')
    for tag in tags_array:
        try:
            t = models.Tags.objects.get(name=tag)
        except Tags.DoesNotExist:
            # 如果标签不存在则新增标签
            t = models.Tags.objects.create(name=tag)
        new_article.tags.add(t)
    return redirect('/article/detail/' + str(new_article.id))


# 文章删除请求
def article_delete_request(request, article_id):
    manage_flag = request.user.is_superuser
    if manage_flag:
        blog = models.Article.objects.get(id=article_id)
        blog.del_flag = True
        blog.save()
        return redirect('/user/backstage/manage/article')
    else:
        return redirect('/')
