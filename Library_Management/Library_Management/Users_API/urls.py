from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (UserDbAPIviewsets)

router = DefaultRouter()
router.register('user', UserDbAPIviewsets, basename='user')

urlpatterns = []
urlpatterns += router.urls