# Generated by Django 5.0.2 on 2024-02-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='password',
            field=models.CharField(max_length=256, verbose_name='Contraseña'),
        ),
    ]
