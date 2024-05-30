from django.urls import path
from . import views

app_name="BuyIt"


urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:it>", views.item,name="item")
]