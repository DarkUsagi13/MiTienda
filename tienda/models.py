from django.db import models
from django.db.models import PROTECT


# Create your models here.

class Marca(models.Model):
    marca = models.CharField(max_length=20)

    def __str__(self):
        return self.marca


class Producto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=PROTECT)
    nombre = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    unidades = models.IntegerField(default=0)
    precio = models.FloatField(default=0)
    detalles = models.TextField(blank=True, max_length=255)

    def __str__(self):
        return self.nombre
