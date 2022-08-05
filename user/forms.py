from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class AuthorRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    bio = forms.CharField(label='Biography', required=False,
                          widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio']
        
    
