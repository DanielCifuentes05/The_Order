from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import TemplateView, DetailView, UpdateView , CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from restaurante.models import Restaurante

# Create your views here.
class UsuarioLogin(LoginView):
    template_name = "user/loginUsuario.html"

    def get_success_url(self):
        return reverse_lazy("usuario:cuentaInicio")

class Landing(TemplateView):
    template_name = "inicio.html"
    
class UsuarioCreate(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('usuario:login')
    template_name = 'user/crearUsuario.html'

class UsuarioInicio(TemplateView):
    template_name = "user/inicioUsuario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurante = Restaurante.objects.filter(user = self.request.user)
        print("Restaurante", restaurante)
        context['restaurantes'] = restaurante
        return context 

