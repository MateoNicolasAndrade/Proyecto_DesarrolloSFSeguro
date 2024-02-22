from rest_framework import serializers
from login.models import UserDb

class UserDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDb
        fields = '__all__'