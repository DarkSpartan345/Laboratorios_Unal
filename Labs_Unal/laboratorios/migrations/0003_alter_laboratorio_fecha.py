# Generated by Django 5.1.1 on 2024-10-19 20:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0002_laboratorio_imagen_laboratorio_materiales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
