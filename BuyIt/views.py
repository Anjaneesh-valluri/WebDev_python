from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import generics
from .serializer import ProductModelSerializer

 

# Create your views here.
app_name='BuyIt'

def index(request):
    Product1= Product.objects.all()
    return render(request, "BuyIt/index.html",{'Products' : Product1})

def item(request,it):
    items= Product.objects.get(id=it)
    return render(request, "BuyIt/item.html",{'items' : items})

def about(request):
    return render(request,"BuyIt/about.html")
    
def profile(request):
    user = request.user
    user = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
            'last_login' : user.last_login
        }
    if request.method == "POST":
        name = request.POST["name"]
        img = request.POST["image"]
        tag = request.POST["tag"]
        price = request.POST["price"]
        desc = request.POST["desc"]

        if Product.objects.filter(name=name).exists():
            messages.info("Already exists")
            return redirect("BuyIt:profile")
        else:
            product = Product.objects.create(name = name,img = img,  tag = tag, desc = desc ,  price = price)
            product.save()
            messages.info("Product added")
            return redirect("BuyIt:profile")
    else:
       return render(request, "BuyIt/profile.html",{})
    return render(request, "BuyIt/profile.html", user)

def contact(request):
    return render(request, "BuyIt/contact.html")


class ProductModelViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer