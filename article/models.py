from django.db import models
from django.contrib.auth.models import User


# 数据模型设计好之后，我们就需要迁移数据到数据库。我们运行如下命令：
# python manage.py makemigrations
# python manage.py migrate
class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    然后给name设置了一个'分类'的名称
    """
    name = models.CharField('分类', max_length=100)


class Tags(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField('标签', max_length=100)


class Article(models.Model):
    # 文章正文，我们使用了 TextField，并且指定了标题的长度
    title = models.CharField('标题', max_length=70)
    # 标题图
    image_url = models.CharField('标题图', max_length=500, blank=True)
    # 使用 TextField 来存储大段文本，文章摘要，我们指定了最大长度和允许可以为空。
    intro = models.TextField('摘要', max_length=200, blank=True)
    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 category 指定了 blank=True。
    # 文章分类，我们还使用了on_delete参数，这个是Django2.0强制ForeignKey必须使用的。
    # 具体更多的资料可以查看官网，也可以查看Django2.0外键参数on_delete的使用方法：https://www.django.cn/article/show-6.html
    # 后面我们也会有专门的文章对一对多、多对多进行详细介绍
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    tags = models.ManyToManyField(Tags, blank=True)
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    # created_time，我们使用了DateTimeField字段，添加了一个auto_now_add参数，自动获取添加时间！
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    # 点击数
    hits = models.IntegerField('点击数')
