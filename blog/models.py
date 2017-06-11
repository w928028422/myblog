from django.db import models
from django.contrib.auth.admin import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.
class Tags(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)

    #文章正文
    body = models.TextField()

    #创建时间
    create_time = models.DateTimeField()
    #最后修改时间
    modify_time = models.DateTimeField()

    #文章摘要，允许为空
    excerpt = models.CharField(max_length=200, blank=True)

    #作者
    author = models.ForeignKey(User)

    #分类
    category = models.ForeignKey(Category)
    #标签
    tags = models.ManyToManyField(Tags, blank=True)

    #浏览量
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-create_time']