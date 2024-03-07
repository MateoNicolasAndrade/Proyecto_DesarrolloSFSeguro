from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from login.models import UserDb
from .serializers import UserDbSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password



# Create your views here.

class UserDbAPIviewsets(viewsets.ModelViewSet):
    queryset = UserDb.objects.all()
    serializer_class = UserDbSerializer
    
class UserLoginAPIview(generics.GenericAPIView):
    queryset = UserDb.objects.all()
    serializer_class = UserDbSerializer
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        print(email)
        print(password)
        
        try:
            user = UserDb.objects.get(email=email)
            print(user.email)
            if user.email == email:
                print('El usuario existe')
        except UserDb.DoesNotExist:
            return Response({'error': 'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)
        if check_password(password, user.password):
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)


