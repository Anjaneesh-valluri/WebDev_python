from django.shortcuts import render,get_object_or_404, render
from .cart import Cart
from BuyIt.models import Product
from django.http import JsonResponse

# Create your views here.
app_name='cart'


def cart_summary(request):
    cart = Cart(request)
    products= cart.get_prod
    cart_total = cart.cart_total()
    return render(request,"cart/cart_summary.html",{"products": products, 'cart_total':cart_total})

def cart_update(request):
    return render(request,"cart/cart_summary.html",{})

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')== 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id= product_id)
        print(product)
        cart.add(product=product)
        cart_quantity = cart.__len__()
        cart_total = cart.cart_total()
        response = JsonResponse({ 'Qty':cart_quantity , 'cart_total':cart_total})
        return response

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')== 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product = product_id)
        response = JsonResponse({'deleted':product_id})
        return response

