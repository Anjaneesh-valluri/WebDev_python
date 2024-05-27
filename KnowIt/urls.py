from django.urls import path
from . import views

app_name="KnowIt"

urlpatterns = [
    path("", views.index, name="index"),
    path("physicists/", views.physicists, name="physicists"),
    path("form/",views.form,name="form"),
    path("form/display/",views.display,name="display")
]