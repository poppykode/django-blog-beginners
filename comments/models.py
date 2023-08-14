from django.db import models
from django.db.models.deletion import CASCADE
from posts.models import Post
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,related_name="user_comment")
    post = models.ForeignKey(Post,on_delete=CASCADE,related_name='post_comment')
    comment =models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
    
    class Meta:
        ordering = ["-timestamp", ]

