from django import forms 
from .models import Restaurante , Producto , Orden

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = [
            'nombre',
            'descripcion',
            'logo'
        ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'precio',

        ]

class OrdenForm(forms.ModelForm):
    class Meta:
        model= Orden
        fields= [
            'nombre',
            'empaque',
            'observaciones'
        ]