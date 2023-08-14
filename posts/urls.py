from django.urls import path
from . import views

app_name ='posts'

urlpatterns = [
    path('all',views.posts,name='posts'),
    path('post/details/<int:blog_id>',views.post,name='post'),
    path('add-post',views.add_post,name='add_post'),
    path('delete-post/<int:id>',views.delete_post,name='delete_post'),
]