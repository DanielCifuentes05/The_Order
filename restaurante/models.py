from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, null = True, blank = True)
    logo = models.ImageField(upload_to = "logos_restaurantes/", null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.descripcion}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, null = True, blank = True)
    precio = models.FloatField()
    restaurante = models.ForeignKey(Restaurante ,on_delete = models.CASCADE )