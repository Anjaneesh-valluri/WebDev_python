from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
import copy
from cart.cart import Cart
from django_prac import settings

# Create your views here.

def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("members:mugen")
        else:
           messages.success(request,("Please enter right username/password and try again!!"))
           return redirect("members:login_user")
    else:
     return render(request, "members/login_user.html", {})


def register_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password =request.POST["password"]
        password1 = request.POST["re-password"]
        if User.objects.filter(username=username).exists():
           messages.info(request,"Username is already taken, please try with other username")
           return redirect("members:register_user")
        elif User.objects.filter(email=email).exists():
           messages.info(request,"Sorry! Email already exists, try giving another one")
           return redirect("members:register_user")
        elif password==password1:
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.info(request,"Congrats!! User created successfully")
            return redirect("members:register_user")
        else:
           messages.info(request,"Passwords dosent match, please re-enter")
           return redirect("members:register_user")
    else:
       return render(request, "members/register_user.html",{})

def logout_user(request):
   cart = copy.deepcopy(Cart(request).cart)
   session = request.session
   print(session.get('session_key'))
   session.modified = True
   messages.success(request,("Successfully logged out!!"))
   logout(request)
   return redirect("members:login_user")

def mugen(request):
   messages.success(request,("You are successfully logged in!!"))
   return render(request, "members/mugen.html",{})

def update_user(request):
   
   return(request, "members/update_user.html",{})