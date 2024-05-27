from django.shortcuts import render
from django.http import HttpResponse


form1 = []
def index(request):
    return render(request,"KnowIt/index.html")
def physicists(request):
    return render(request,"KnowIt/physicists.html")
def form(request):
    if request.method=="Post":
        form1= request.post
        return render(request,"KnowIt/display.html",{"form":form1})
    return render(request,"KnowIt/form.html")

def display(request):
    email = request.GET['inlineFormInputGroupUsername']
    #value = request.GET['inlineFormCheck']
    form = [email]


    return render(request,"KnowIt/display.html",{"form": form})