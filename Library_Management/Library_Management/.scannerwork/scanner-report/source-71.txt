from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from login.models import UserDb
from .serializers import UserDbSerializer

# Create your views here.

class UserDbAPIviewsets(viewsets.ModelViewSet):
    queryset = UserDb.objects.all()
    serializer_class = UserDbSerializer
    

