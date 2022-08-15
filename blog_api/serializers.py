from datetime import datetime
from rest_framework import serializers
from user.models import Author, User
from blog.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', ]


class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'user', ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'description',
                  'is_published', 'author', ]

    def to_representation(self, instance):
        self.fields['author'] = AuthorSerializer(read_only=True)
        return super(PostSerializer, self).to_representation(instance)

    def create(self, validated_data):
        validated_data['created_at'] = datetime.now()
        return super(PostSerializer, self).create(validated_data)
