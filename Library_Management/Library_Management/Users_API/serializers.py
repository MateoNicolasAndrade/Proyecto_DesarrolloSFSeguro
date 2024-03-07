from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import authenticate
from login.models import UserDb

class UserDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDb
        fields = '__all__'
        
    
class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user 