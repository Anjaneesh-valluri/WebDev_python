from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth

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
    if request.method=="POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password =request.POST["password"]
        password1 = request.POST["re-password"]
        if password==password1:
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,("Account created successfully.... Please log in..."))
            return redirect("members:register_user")
        else:
           messages.success(request,("Entered password does'nt match the above one"))
           return render(request,"members/register_user.html",{})
    else:
       return render(request, "members/register_user.html",{})

def logout_user(request):
   messages.success(request,("Successfully logged out!!"))
   logout(request)
   return redirect("members:login_user")