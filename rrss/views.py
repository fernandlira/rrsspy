from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, CommentSerializer, FollowSerializer
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment, Follow
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'first_name')

class PostView(viewsets.ViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        post = Post.objects.create(user=request.user,image=request.data['image'],caption=request.data['caption'])
        post.save()
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=False)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CommentView(viewsets.ViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        comment = Comment.objects.create(user=request.user,post_id=int(request.data['id']),comment=request.data['comment'])
        comment.save()
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=False)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

class FollowView(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def list(self, request):
        queryset = Follow.objects.all()
        serializer = FollowSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        post = Follow.objects.create(following_id=int(request.data['id']), followed_id=int(request.data['id']))
        post.save()
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = Follow.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = FollowSerializer(comment, data=request.data, partial=False)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Follow.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = FollowSerializer(comment, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)