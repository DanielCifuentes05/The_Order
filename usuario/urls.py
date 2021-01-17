from django.urls import path, reverse_lazy
from .views import CrearUsuario, LoginUsuario , Inicio
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, 
    PasswordResetDoneView, PasswordResetConfirmView
)
from django.contrib.auth.decorators import login_required

app_name = 'usuario'

urlpatterns = [
    path('signup/', CrearUsuario.as_view(), name = "signup"),
    path('login/', LoginUsuario.as_view(), name = "login"),
    path('perfil/', login_required(Inicio.as_view(), login_url=reverse_lazy("usuario:login")), name = "cuentaInicio"),
]