from app.models import (
    User,
    Category,
    Tag,
    Post
)
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='title',
        required=False
    )
    
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title',
        allow_null=True,
        required=False
    )

    author = UserSerializer(read_only=True)
    

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author',
            'category',
            'tags',
            'published',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['title']