from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
 

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
    return render(request, "BuyIt/profile.html", user)
