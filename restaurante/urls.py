from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import RestauranteCreate , RestauranteInicio

app_name = 'restaurante'

urlpatterns = [
    path('crearRestaurante/', login_required(RestauranteCreate.as_view() , login_url=reverse_lazy("usuario:login")), name = "crearRestaurante"),
    path('inicioRestaurante/<int:pk>/',login_required(RestauranteInicio.as_view() , login_url=reverse_lazy("usuario:login")) , name = "inicioRestaurante"),
]

