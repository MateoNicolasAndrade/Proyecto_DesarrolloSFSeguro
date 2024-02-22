from django.urls import path
from .views import index_view, api_user_read


urlpatterns = [
    path('simple/',index_view),
    path('api/user-read/',api_user_read, name='api_user_read')
]