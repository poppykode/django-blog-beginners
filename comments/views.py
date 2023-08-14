from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from .models import Comment

# Create your views here.
def comments(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    Comment.objects.create(
        post=post,
        comment = request.POST.get('comment')
    )
    return redirect('blog:post', post_id)

