"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path

from .forms import AuthorLoginForm
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', next_page='post_list', authentication_form=AuthorLoginForm), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
