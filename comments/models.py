from django.db import models

# Create your models here.
class Comment(models.Model):

    #昵称
    name = models.CharField(max_length=100)
    #邮箱
    email = models.CharField(max_length=255)
    #个人网站
    url = models.URLField(blank=True)
    #评论内容
    text = models.TextField()
    #评论时间
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
