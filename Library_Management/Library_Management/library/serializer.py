from rest_framework import serializers
from .models import Estudiante, Prestamo, Autor, Libro, DetallePrestamo

#Serializadores para los modelos

class EstudianteSerializer(serializers.ModelSerializer):
    '''Serializador para el modelo de estudiantes'''
    class Meta:
        model = Estudiante
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    '''Serializador para el modelo de prestamos'''
    class Meta:
        model = Prestamo
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    '''Serializador para el modelo de autores'''
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    '''Serializador para el modelo de libros'''
    autor_id = AutorSerializer()
    
    class Meta:
        model = Libro
        fields = '__all__'

class DetallePrestamoSerializer(serializers.ModelSerializer):
    '''Serializador para el modelo de detalles de prestamos'''

    autor = AutorSerializer()
    libro = LibroSerializer()
    estudiante = EstudianteSerializer()
    prestamo = PrestamoSerializer()

    class Meta:
        model = DetallePrestamo
        fields = '__all__'