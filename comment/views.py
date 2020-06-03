from django.shortcuts import render, redirect
from comment import models
from django.http import HttpResponse
import json


# 新增评论
def create_article_comment(request):
    # 如果用户未登录则跳登录页面
    user = request.user
    if user.username == '':
        return redirect('/user/login')
    article_id = request.GET.get("article_id")
    comment_content = request.GET.get("content")
    models.Comment.objects.create(data_id=article_id, content=comment_content, user=user)
    # 返回到文章详情页面
    return redirect('/article/detail/' + str(article_id))


# 回复评论
def create_comment_child(request):
    # 如果用户未登录则跳登录页面
    user = request.user
    if user.username == '':
        return redirect('/user/login')

    comment_id = request.GET.get("comment_id")
    comment_content = request.GET.get("content")
    comment = models.Comment.objects.get(id=comment_id)
    models.Comment_child.objects.create(parent_id=comment_id, content=comment_content, user=user)
    # 返回到文章详情页面
    return redirect('/article/detail/' + str(comment.data_id))


def get_article_comment(request, article_id):
    comments = models.Comment.objects.filter(data_id=article_id).all().order_by('-id')
    result = []
    for comment in comments:
        child_comment = models.Comment_child.objects.filter(parent_id=comment.id).all().order_by('id')
        child_result = []
        if child_comment is not None:
            for child in child_comment:
                ct = {
                    'content': child.content,  # 评论内容
                    'id': child.id,  # id
                    'username': child.user.username,  # 作者名
                    'created_time': child.created_time.strftime("%Y-%m-%d %H:%M:%S"),  # 创建时间
                    'avatar': child.user.avatar,  # 用户头像
                }
                child_result.append(ct)
        context = {
            'content': comment.content,  # 评论内容
            'id': comment.id,  # id
            'username': comment.user.username,  # 作者名
            'created_time': comment.created_time.strftime("%Y-%m-%d %H:%M:%S"),  # 创建时间
            'avatar': comment.user.avatar,  # 用户头像
            'child_comment': child_result,  # 子评论
        }
        result.append(context)
    return HttpResponse(json.dumps({
        "comments": result,
    }))
