from rest_framework import viewsets
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Comment, Follow
from rest_framework import filters

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'name')