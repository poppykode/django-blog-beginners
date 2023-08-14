from django.shortcuts import render,redirect
from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User

from blog.utils import generate_password

from .decorators import is_authenticated

# Create your views here.

@is_authenticated
def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                messages.error(
                    request, 'Your account has been deactivate, please contact Sketchy.')
                return render(request, template_name)
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('accounts:redirect_logged')
        messages.error(request, 'Invalid username or password.')
    return render(request, template_name)

@login_required
def redirect_logged(request):
    return redirect('posts:posts')

def user_logout(request):
    auth.logout(request)
    messages.info(request,'Logged out Successfully!')
    return redirect('/')

def register(request,role):
    template_name = 'register.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = ''
        is_admin = False
        is_user = False
        if role == 'user':
            is_user = True
            role = 'user'
        # else:
        #     is_admin = True
        #     role = 'admin'
        new_user= User.objects.create(
            username=username,
            email=request.POST.get('email'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            role=role,
            is_user = is_user,
            is_admin = is_admin
        )
        # password_ = generate_password()
        new_user.set_password(password)
        new_user.save()
        ##send
        if new_user:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully register an account.')
                return redirect('accounts:redirect_logged')
    return render(request, template_name)
