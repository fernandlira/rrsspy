from django.urls import path, include
from rest_framework import routers
from .views import UserView, PostView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('post', PostView)

urlpatterns = [
    path('api/', include(router.urls)),
]