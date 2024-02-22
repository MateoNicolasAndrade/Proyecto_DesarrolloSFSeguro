from django.contrib import admin
from django.urls import path, include
from login.views import indexView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('simple/',indexView),
    path('',include("library.urls")),
    path('',include("Users_API.urls")),
]

