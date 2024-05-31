from django.shortcuts import render,get_object_or_404, render
from .cart import Cart
from BuyIt.models import Product
from django.http import JsonResponse

# Create your views here.
app_name='cart'


def cart_summary(request):
    return render(request,"cart/cart_summary.html",{})

def cart_update(request):
    return render(request,"cart/cart_summary.html",{})

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')== 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id= product_id)
        print(product)
        cart.add(product=product)
        response = JsonResponse({ 'Product Name: ':product.name})
        return response

def cart_delete(request):
    return render(request,"cart/cart_summary.html",{})
