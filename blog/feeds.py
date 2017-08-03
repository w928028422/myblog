from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    title_template = "暗影之龙的博客"
    link = "/"
    description_template = "暗影之龙的博客文章"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{0}] {1}'.format(item.category, item.title)

    def item_description(self, item):
        return item.body
