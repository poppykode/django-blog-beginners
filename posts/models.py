from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,related_name="user_post")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def get_full_name(self):
    #     return self.first_name + ' ' +self.last_name

    def __str__(self):
        return self.title + ' '+ str(self.timestamp)
    
    class Meta:
        ordering = ["-timestamp", ]



