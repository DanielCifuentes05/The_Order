from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import RestauranteCreate , RestauranteInicio , ProductoCreate , ProductoList , OrdenCreate , DoneOrden

app_name = 'restaurante'

urlpatterns = [
    path('crearRestaurante/', login_required(RestauranteCreate.as_view() , login_url=reverse_lazy("usuario:login")), name = "crearRestaurante"),
    path('inicioRestaurante/<int:pk>/',login_required(RestauranteInicio.as_view() , login_url=reverse_lazy("usuario:login")) , name = "inicioRestaurante"),
    path('crearProducto/<int:pk>/',login_required(ProductoCreate.as_view() , login_url=reverse_lazy("usuario:login")) , name = "crearProducto"),
    path('listarProducto/<int:pk>/',login_required(ProductoList.as_view() , login_url=reverse_lazy("usuario:login")) , name = "listarProducto"),
    path('crearOrden/<int:pk>/',login_required(OrdenCreate.as_view() , login_url=reverse_lazy("usuario:login")) , name = "crearOrden"),
    path('doneOrden/<int:pk>/',login_required(DoneOrden.as_view() , login_url=reverse_lazy("usuario:login")) , name = "doneOrde")
]

