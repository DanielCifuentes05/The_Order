from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import (RestauranteCreate , RestauranteInicio , ProductoCreate, 
                   ProductoList , OrdenCreate , DoneOrden , OrdenList , orden_status_update)

app_name = 'restaurante'

urlpatterns = [
    path('crearRestaurante/', login_required(RestauranteCreate.as_view() , login_url=reverse_lazy("usuario:login")), name = "crearRestaurante"),
    path('inicioRestaurante/<int:pk>/',login_required(RestauranteInicio.as_view() , login_url=reverse_lazy("usuario:login")) , name = "inicioRestaurante"),
    path('crearProducto/<int:pk>/',login_required(ProductoCreate.as_view() , login_url=reverse_lazy("usuario:login")) , name = "crearProducto"),
    path('listarProducto/<int:pk>/',login_required(ProductoList.as_view() , login_url=reverse_lazy("usuario:login")) , name = "listarProducto"),
    path('crearOrden/<int:pk>/',login_required(OrdenCreate.as_view() , login_url=reverse_lazy("usuario:login")) , name = "crearOrden"),
    path('doneOrden/<int:pk>/',login_required(DoneOrden.as_view() , login_url=reverse_lazy("usuario:login")) , name = "doneOrde"),
    path('listarOrden/<int:pk>/',login_required(OrdenList.as_view() , login_url=reverse_lazy("usuario:login")) , name = "listarOrden"),
    path('statusOrden/<orden_id>/',login_required(orden_status_update , login_url=reverse_lazy("usuario:login")) , name = "statusOrden")
]

