from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from .models import Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_comment(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    Comment.objects.create(
        post=post, 
        user= request.user, 
        comment = request.POST.get('comment')
    )
    messages.success(request, 'You have successfully commented')
    return redirect('posts:post', post_id)

