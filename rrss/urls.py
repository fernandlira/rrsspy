from django.urls import path, include
from rest_framework import routers
from .views import UserView, PostView,FollowView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('post', PostView)
router.register('follow', FollowView)
urlpatterns = [
    path('api/', include(router.urls)),
]