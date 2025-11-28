from django.shortcuts import render
from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostListSerializer, PostDetailSerializer

class PostViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

     def get_queryset(self):
        return Post.objects.select_related('category').prefetch_related('tags')

     def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer   