from django.urls import path
from .views import indexView, ApiUserRead


urlpatterns = [
    path('simple/',indexView),
    path('api/user-read/',ApiUserRead, name='api_user_read')
]