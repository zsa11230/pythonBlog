from django.db import models
from django.contrib.auth.models import User


# 评论对象
class Comment(models.Model):
    # 评论类型，默认为文章评论
    category = models.IntegerField('评论类型，默认为文章评论', default=1)
    # 对应数据ID
    data_id = models.IntegerField('对应数据ID', default=0)
    # 评论内容
    content = models.CharField('评论内容', max_length=500)
    # 创建时间，我们使用了DateTimeField字段，添加了一个auto_now_add参数，自动获取添加时间！
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    # 创建人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')
    # 逻辑删除标记
    del_flag = models.BooleanField('逻辑删除标记', default=False)


# 评论子对象
class CommentChild(models.Model):
    # 父级评论ID
    parent_id = models.IntegerField('父级评论ID', default=0)
    # 评论内容
    content = models.CharField('评论内容', max_length=500)
    # 创建时间，我们使用了DateTimeField字段，添加了一个auto_now_add参数，自动获取添加时间！
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    # 创建人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')
    # 逻辑删除标记
    del_flag = models.BooleanField('逻辑删除标记', default=False)