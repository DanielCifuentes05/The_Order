from django.db import models
from django.contrib.auth.models import User
from PIL import Image


STATUS_ORDEN = [('ESPR' , 'En Espera') , 
                ('PREP', 'En Preparacion'), 
                ('REDY','Listo')]

EMPAQUE = [('IN','Consumir en el sitio'), 
            ('OU','Para llevar')]

# Create your models here.

class Restaurante(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300, null = True, blank = True)
    logo = models.ImageField(upload_to = "logos_restaurantes/", default = "logos_restaurantes/mazda.jpg",  null = True, blank = True)
    user = models.ForeignKey(User ,on_delete = models.CASCADE ,null = True, blank = True)

    def __str__(self):
        return f'{self.nombre} {self.descripcion}'

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400, null = True, blank = True)
    precio = models.FloatField()
    restaurante = models.ForeignKey(Restaurante ,on_delete = models.CASCADE , null = True, blank = True)


#ORDENES

class Orden(models.Model):
    nombre = models.CharField(max_length = 200)
    valor = models.FloatField(null = True, blank = True)
    status = models.CharField(max_length = 4 ,choices = STATUS_ORDEN, default ='ESPR')
    restaurante = models.ForeignKey(Restaurante ,on_delete = models.CASCADE , null = True, blank = True)
    empaque = models.CharField(max_length = 2 ,choices = EMPAQUE, default ='IN')
    observaciones = models.CharField(max_length = 400, null = True, blank = True)

class ItemOrden(models.Model):
    producto = models.ForeignKey(Producto ,on_delete = models.CASCADE ,null = True, blank = True)
    orden = models.ForeignKey(Orden ,on_delete = models.CASCADE ,null = True, blank = True)
    valor = models.FloatField()
    cantidad = models.PositiveIntegerField()
    valor_total = models.FloatField()
    
