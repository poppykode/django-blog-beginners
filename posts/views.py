import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
@login_required
def posts(request):
    template_name = 'posts.html'
    posts = Post.objects.all()[:2]
    data ={
        'posts':posts

    }
    return render(request,template_name,data)

@login_required
def post(request,blog_id):
    template_name = 'post_details.html'
    post = Post.objects.get(id=blog_id)
    context = {
        'post':post
    }
    return render(request, template_name,context)

@login_required
def add_post(request):
    template_name = 'add_post.html'
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        print(form.errors.as_data())
        print(form)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
        # new_post = Post.objects.create(
        # title = request.POST['title'],
        # image =  request.FILES.get('image'),
        # description =  request.POST.get('description')
        # )
        messages.info(request,'Post successfully created.')
        return redirect('posts:posts')
    form = PostForm()
    return render(request, template_name,{'form':form})

@login_required
def delete_post(request, id):
    template_name = 'delete_post.html'
    obj = Post.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        messages.info(request,'Post with title "{}" was successfully deleted.'.format(obj.title))
        return redirect('posts:posts')
    return render(request, template_name,{'obj':obj})
