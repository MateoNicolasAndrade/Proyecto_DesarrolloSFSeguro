from django.db import models

# Create your models here.

class UserDb(models.Model):
    '''The model is for registering users'''
    name = models.CharField(max_length=35, verbose_name='Nombre')
    lastname = models.CharField(max_length=35, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo electrónico')
    password = models.CharField(max_length=35, verbose_name='Contraseña')
    role = models.CharField(max_length=35, verbose_name='Rol')
    
    class Meta:
        db_table = 'USUARIO'
        verbose_name = 'USUARIO'
        verbose_name_plural = 'USUARIOS'
        
    def __str__(self) -> str:
        return self.name + ' ' + self.lastname
