from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ['id','name','slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class PostListSerializer(serializers.ModelSerializer):
    excerpt = serializers.SerializerMethodField()
    
    def get_excerpt(self, obj):
        if obj.excerpt:
            return obj.excerpt
        return obj.content[:300] + "more..." if len(obj.content) > 300 else obj.content
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'excerpt', 'created_at']

class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'