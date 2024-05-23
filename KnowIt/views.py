from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"KnowIt/index.html")
def second(request):
    return render(request,"KnowIt/second.html")