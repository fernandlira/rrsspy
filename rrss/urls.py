from django.urls import path, include
from rest_framework import routers
from .views import UserView, PostView,FollowView, CommentView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('post', PostView)
router.register('follow', FollowView)
router.register('comment', CommentView)
urlpatterns = [
    path('api/', include(router.urls)),
]
