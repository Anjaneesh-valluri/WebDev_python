from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    container1 = models.container()
    container1.id=1
    container1.name= "Mobile"
    container1.desc= "Electronic device"
    container1.price = 50000


    return render(request, "BuyIt/index.html",{'container': container1})