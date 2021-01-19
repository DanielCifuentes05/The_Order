from django.shortcuts import render
#Tomado de : https://github.com/Palash51/food/blob/master/cart/cart.py

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from restaurante.models import Producto 
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(producto=product,
                 quantity=cd['cantidad'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail' , pk =product.restaurante.id )


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail' , pk = product.restaurante.id)


def cart_detail(request , pk):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'cantidad': item['quantity'],
                'update': True
            })
    totalpedido = cart.get_total_price()
    return render(request, 'cart/detalleCart.html', {'cart': cart , 'restaurante' : pk , 'totalpedido' : totalpedido})