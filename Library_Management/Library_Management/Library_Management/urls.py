from django.contrib import admin
from django.urls import path
from login.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/',indexView),
]

