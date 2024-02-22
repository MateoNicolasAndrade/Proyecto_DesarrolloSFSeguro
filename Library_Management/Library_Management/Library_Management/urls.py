from django.contrib import admin
from django.urls import path, include
from login.views import index_view

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('simple/',index_view),
    path('',include("library.urls")),
    path('',include("Users_API.urls")),
]

