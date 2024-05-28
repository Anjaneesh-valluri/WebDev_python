from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("KnowIt:index")
        else:
           messages.success(request,("Please enter right username/password and try again!!"))
           return redirect("members:login_user")
    else:
     return render(request, "members/login_user.html", {})


def register_user(request):
   return render(request, "members/register_user.html",{})

def logout_user(request):
   messages.success(request,("Successfully logged out!!"))
   logout(request)
   return redirect("members:login_user")