from django.db import models

# Create your models here.

class Estudiante(models.Model):
    '''Modelo de registro de estudiantes'''
    estudiante_nombre = models.CharField(max_length=35, verbose_name='Estudiante_nombre')
    estudiante_correo = models.EmailField(verbose_name='Estudiante_correo')
    
    class Meta:
        db_table = 'ESTUDIANTE'
        verbose_name = 'ESTUDIANTE'
        verbose_name_plural = 'ESTUDIANTES'
        
    def __str__(self) -> str:
        return self.estudiante_nombre + ' ' + self.estudiante_correo

class Prestamo(models.Model):
    '''Modelo de registro de prestamos de libros'''
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante_id')
    prestamo_fechaEnt = models.DateField(verbose_name='Fecha_Entrega', null=False, blank=False)
    prestamo_fechaDev = models.DateField(verbose_name='Fecha_Devolucion', null=False, blank=False)
    
    class Meta:
        db_table = 'PRESTAMO'
        verbose_name = 'PRESTAMO'
        verbose_name_plural = 'PRESTAMOS'
        
    def __str__(self) -> str:
        return self.estudiante + ' ' + self.prestamo_fechaEnt + ' ' + self.prestamo_fechaDev

class Autor(models.Model):
    '''Modelo de registro de autores de libros'''
    autor_nombre = models.CharField(max_length=35, verbose_name='Autor_nombre')
    
    class Meta:
        db_table = 'AUTOR'
        verbose_name = 'AUTOR'
        verbose_name_plural = 'AUTORES'
        
    def __str__(self) -> str:
        return self.autor_nombre

class Libro(models.Model):
    '''Modelo de registro de libros'''
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    libro_nombre = models.CharField(max_length=35, verbose_name='Libro_nombre')
    
    
    class Meta:
        db_table = 'LIBRO'
        verbose_name = 'LIBRO'
        verbose_name_plural = 'LIBROS'
        
    def __str__(self) -> str:
        return self.libro_nombre + ' ' + self.autor_id

class DetallePrestamo(models.Model):
    '''Modelo de registro de detalles de prestamos de libros'''
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name='Libro')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, verbose_name='Prestamo')
    
    
    class Meta:
        db_table = 'DETALLE_PRESTAMO'
        verbose_name = 'DETALLE_PRESTAMO'
        verbose_name_plural = 'DETALLES_PRESTAMOS'
        
    def __str__(self) -> str:
        return self.libro + ' ' + self.autor + ' ' + self.estudiante + ' ' + self.prestamo
    