from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User


class AuthorRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    bio = forms.CharField(label='Biography', required=False,
                          widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio']
        
class AuthorLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    
