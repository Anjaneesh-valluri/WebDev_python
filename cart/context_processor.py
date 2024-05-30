from .cart import Cart

def cart(request):
    return {'Cart': Cart(request)}