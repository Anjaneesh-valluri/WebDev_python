from django.contrib import admin
from django.urls import include,path
from . import views

app_name="members"

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("logout_user",views.logout_user,name="logout_user"),
    path("register_user",views.register_user,name="register_user"),
    path("mugen",views.mugen,name="mugen"),
    path("update_user", views.update_user, name="update_user")
]