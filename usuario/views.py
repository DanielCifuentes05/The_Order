from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import TemplateView, DetailView, UpdateView , CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
class LoginUsuario(LoginView):
    template_name = "user/login.html"

    def get_success_url(self):
        return reverse_lazy("usuario:cuentaInicio")

class Landing(TemplateView):
    template_name = "inicio.html"
    
class CrearUsuario(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('usuario:login')
    template_name = 'user/crearUsuario.html'

class Inicio(TemplateView):
    template_name = "user/cuentaInicio.html"
