from django.urls import path, reverse_lazy
from django.contrib.auth.views import  LogoutView 
    

from django.contrib.auth.decorators import login_required
from .views import UsuarioCreate, UsuarioLogin, UsuarioInicio

app_name = 'usuario'

urlpatterns = [
    path('signup/', UsuarioCreate.as_view(), name = "signup"),
    path('login/', UsuarioLogin.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(next_page = reverse_lazy("usuario:login")), name = 'logout'),
    path('perfil/', login_required(UsuarioInicio.as_view(), login_url=reverse_lazy("usuario:login")), name = "cuentaInicio"),
]