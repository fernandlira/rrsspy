from rest_framework import serializers
from .models import Post, Comment, Follow
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']



class PostSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    #userId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())
    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    #userId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())
    #post = PostSerializer(read_only=True)
    #postId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = "__all__"

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"
