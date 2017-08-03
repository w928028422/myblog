from django.db import models
from users.models import User

# Create your models here.
class Comment(models.Model):

    user = models.OneToOneField('users.User')
    #评论内容
    text = models.TextField()
    #评论时间
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
