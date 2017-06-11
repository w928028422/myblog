from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_pk):

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            #如果数据合法，保存到数据库
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)

        else:
            #如果数据不合法，重新渲染详情页
            comment_list = post.comment_set.all()
            context = {'post':post, 'form':form, 'comment_list':comment_list}
            return render(request, 'detail.html', context=context)

    return request(post)
