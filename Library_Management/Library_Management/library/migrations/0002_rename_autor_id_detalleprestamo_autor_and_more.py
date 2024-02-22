# Generated by Django 5.0.2 on 2024-02-22 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='autor_id',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='estudiante_id',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='libro_id',
            new_name='libro',
        ),
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='prestamo_id',
            new_name='prestamo',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='estudiante_id',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='autor_id',
            new_name='autor',
        )
        
    ]
