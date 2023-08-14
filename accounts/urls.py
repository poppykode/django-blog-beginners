from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path('',views.login, name='login'),
    path('register/<str:role>',views.register, name='register'),
    path('redirect-logged',views.redirect_logged, name='redirect_logged'),
    path('user-logout',views.user_logout, name='user_logout')
]