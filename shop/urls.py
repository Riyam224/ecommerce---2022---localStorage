from urllib.parse import urlparse
from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path("checkout/",views.checkout, name="checkout"),
    path("about/", views.about, name="about"),
    path('' , views.index , name='index'),
    path('<slug:slug>/' , views.detail , name='detail'),
    
]
