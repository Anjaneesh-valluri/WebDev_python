from django.contrib import admin
from django.urls import include,path
from . import views

app_name="members"

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("logout_user",views.logout_user,name="logout_user")
]