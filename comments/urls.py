from django.urls import path
from . import views

app_name ='comments'

urlpatterns = [
    path('add-comment/<int:post_id>',views.add_comment,name='add_comment')
]
