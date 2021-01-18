from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView , CreateView , ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from .forms import RestauranteForm , ProductoForm
from .models import Restaurante, Producto
from cart.forms import CartAddProductForm
# Create your views here.

class RestauranteCreate(CreateView):
    model = Restaurante
    template_name = 'restaurante/crearRestaurante.html'
    success_url = reverse_lazy("usuario:cuentaInicio")
    form_class = RestauranteForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = RestauranteForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            restaurante = form.save()
            restaurante.user = request.user
            restaurante.save()
            return HttpResponseRedirect(self.success_url)
        else:
            for field in form:
                for error in field.errors:
                    print(error)
            return self.render_to_response(self.get_context_data(form = form))

class RestauranteInicio(TemplateView):
    template_name = "restaurante/inicioRestaurante.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet all the transactions

        restaurante = Restaurante.objects.get(id = self.kwargs['pk'])
        context['restaurante'] = restaurante

        return context

class ProductoCreate(CreateView):
    model = Producto
    template_name = "restaurante/crearProducto.html"
    form_class = ProductoForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = ProductoForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            producto = form.save()
            restaurante = Restaurante.objects.get(id = self.kwargs['pk'])
            producto.restaurante = restaurante
            producto.save()
            return HttpResponseRedirect(reverse_lazy("restaurante:inicioRestaurante" , kwargs={'pk': self.kwargs['pk']}))
        else:
            for field in form:
                for error in field.errors:
                    print(error)
            return self.render_to_response(self.get_context_data(form = form))

class ProductoList(ListView):
    model = Producto
    template_name = 'restaurante/listarProducto.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet all the transactions

        context['form_cart'] = CartAddProductForm()

        return context

    def get_queryset(self):
        restaurante = Restaurante.objects.get(id = self.kwargs['pk'])
        
        return Producto.objects.filter(restaurante = restaurante)
    