from django.urls import path,include
from . import views
from .views import ProductModelViewSet

app_name="BuyIt"

#router = DefaultRouter()
#router.register(r'Product', ProductModelViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:it>", views.item,name="item"),
    path("about/", views.about, name="about"),
    path("profile/",views.profile, name= "profile"),
    path("contact/", views.contact, name = "contact"),
    path('api/products/', ProductModelViewSet.as_view(), name = 'product-list')
]