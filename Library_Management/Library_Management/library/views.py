from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import generics
from .models import Estudiante, Prestamo, Autor, Libro, DetallePrestamo
from .serializer import EstudianteSerializer, PrestamoSerializer, AutorSerializer, LibroSerializer, DetallePrestamoSerializer
from rest_framework import viewsets

# Create your views here.

#vistas api

class EstudianteAPIviewSet(viewsets.ModelViewSet):
    '''Vista para el modelo de estudiantes'''
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class PrestamoAPIviewSet(viewsets.ModelViewSet):
    
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class AutorAPIviewSet(viewsets.ModelViewSet):
    
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroAPIviewSet(viewsets.ModelViewSet):
    
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class DetallePrestamoAPIviewSet(viewsets.ModelViewSet):
        
    queryset = DetallePrestamo.objects.all()
    serializer_class = DetallePrestamoSerializer