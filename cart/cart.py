#Tomado de : https://github.com/Palash51/food/blob/master/cart/cart.py

from restaurante.models import Producto ,ItemOrden


class Cart(object):
    def __init__(self, request):
        #Crea el carrito
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # Si no existe el carrito, se crea uno nuevo en la sesion
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, producto, quantity = 1, update_quantity=False):
        #Adiciona un producto en el carrito o actualiza su cantidad
        product_id = str(producto.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(producto.precio)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Actualiza la sesion del carrito
        self.session['cart'] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, producto):
        product_id = str(producto.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        
        #Itera sobre el carrito y obtiene los productos de la base de datos
        product_ids = self.cart.keys()
        
        products = Producto.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        #Cuenta los items en el carrito
        
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Elimina el carrito de la sesion 
        del self.session['cart']
        self.session.modified = True