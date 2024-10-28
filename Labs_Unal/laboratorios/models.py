from django.db import models
from django.utils import timezone

class Laboratorio(models.Model):
    titulo = models.CharField(max_length=200)  # Título del laboratorio
    descripcion = models.TextField(default='')            # Descripción detallada del laboratorio
    fecha = models.DateTimeField(default=timezone.now)                  # Fecha de realización
    objetivo = models.TextField(default='')                # Objetivo del laboratorio
    materiales = models.TextField(default='')              # Materiales necesarios
    procedimiento = models.TextField(default='')           # Pasos a seguir en el laboratorio
    resultados = models.TextField(null=True, blank=True)  # Resultados esperados
    observaciones = models.TextField(null=True, blank=True)  # Observaciones finales
    imagen = models.ImageField(upload_to='imagenes/laboratorios/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo