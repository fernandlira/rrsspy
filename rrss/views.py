from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, CommentSerializer, FollowSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Comment, Follow
from rest_framework import filters

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'first_name')

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer