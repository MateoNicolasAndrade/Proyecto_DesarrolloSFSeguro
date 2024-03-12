from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import authenticate
from login.models import UserDb

class UserDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDb
        fields = '__all__'
        
    