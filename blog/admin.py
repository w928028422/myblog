from django.contrib import admin
from blog.models import Post, Category, Tags
from comments.models import Comment
from users.models import User

# Register your models here.
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)