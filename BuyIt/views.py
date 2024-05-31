from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
 

# Create your views here.
app_name='BuyIt'

def index(request):
    Product1= Product.objects.all()
    return render(request, "BuyIt/index.html",{'Products' : Product1})

def item(request,it):
    items= Product.objects.get(id=it)
    return render(request, "BuyIt/item.html",{'items' : items})
