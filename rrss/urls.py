from django.urls import path, include
from rest_framework import routers
from .views import UserView, PostView, FollowUser, DeletePost, FollowView
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register('user', UserView)
router.register('post', PostView)
router.register('follow', FollowView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('follow/<int:id>', FollowUser, name='seguir'),
    path('api/login', obtain_jwt_token)
]