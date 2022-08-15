from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import PostSerializer, UserSerializer
from user.models import User
from blog.models import Post


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.select_related('author__user').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
