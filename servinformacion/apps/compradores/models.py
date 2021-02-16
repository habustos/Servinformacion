from django.db import models

class compradores(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True)
    apellido = models.CharField(max_length=100, null=False, unique=True)
    direccion = models.CharField(max_length=100, null=False, unique=True)
    ciudad = models.CharField(max_length=100, null=False, unique=True)
    longitud = models.FloatField(null=False, unique=True)
    latitud = models.FloatField(null=False, unique=True)
    estado_geo = models.CharField(max_length=100, null=False, unique=True)
