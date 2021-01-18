from django.contrib import admin
from .models import Restaurante , Producto , Orden , ItemOrden
# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(ItemOrden)