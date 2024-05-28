from django.urls import path
from . import views

app_name="BuyIt"


urlpatterns = [
    path("", views.index, name="index"),
]