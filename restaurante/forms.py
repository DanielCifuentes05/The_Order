from django import forms 
from .models import Restaurante , Producto

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
