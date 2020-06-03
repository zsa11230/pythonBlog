from django.db import models
from django.contrib.auth.models import AbstractUser


# 重写用户类
class User(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default='')
    avatar = models.CharField(max_length=500, default='')