from django import forms
from . import models


class LoginForm(forms.Form):    
    username = forms.CharField(max_length = 200,) 
    password = forms.CharField(widget = forms.PasswordInput()) 


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        # widgets = {
        #     'exam_date': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date'}),
        # }
        labels = {
            'image':'Upload Post Image'
        }

        fields = ('title','description','image')

