from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
 

# Create your views here.

def index(request):
    Product1= Product.objects.all()
    return render(request, "BuyIt/index.html",{'Products' : Product1})

def cart(request):
    return render(request,"BuyIt/cart.html",{})