# Generated by Django 5.0.2 on 2024-02-22 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_autor_id_detalleprestamo_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.autor', verbose_name='Autor_id'),
        ),
    ]
