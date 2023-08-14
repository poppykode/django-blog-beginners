

from django.shortcuts import redirect

def is_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user and request.user.is_active:
            return redirect('accounts:redirect_logged')
        return view_func(request, *args, **kwargs)
    return wrapper