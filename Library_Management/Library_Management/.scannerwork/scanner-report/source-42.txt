from django.contrib import admin
from .models import UserDb

# Register your models here.

class UserDbAdmin(admin.ModelAdmin):
    '''Class for the UserDb model'''
    fields = ['name', 'lastname', 'password', 'email', 'role']
    list_display = ['name', 'lastname', 'email', 'role']
    
admin.site.register(UserDb, UserDbAdmin)
