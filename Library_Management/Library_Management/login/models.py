"""Module providing a models for login python version."""
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class UserDb(models.Model):
    '''The model is for registering users'''
    name = models.CharField(max_length=35, verbose_name='Nombre')
    lastname = models.CharField(max_length=35, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo electrónico')
    password = models.CharField(max_length=256, verbose_name='Contraseña')
    role = models.CharField(max_length=35, verbose_name='Rol')

    class Meta:
        db_table = 'USUARIO'
        verbose_name = 'USUARIO'
        verbose_name_plural = 'USUARIOS'

    def __str__(self) -> str:
        return self.name + ' ' + self.lastname
    
    def save(self, *args, **kwargs):
        if not self.pk:  # This is a new object, so hash the password
            self.password = make_password(self.password)
        else:  # This is an existing object, so check if the password has changed
            orig = UserDb.objects.get(pk=self.pk)
            if not check_password(self.password, orig.password):
                self.password = make_password(self.password)
        super().save(*args, **kwargs)
