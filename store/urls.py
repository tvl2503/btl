from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store_page"),
    path('cart/', views.cart, name = "cart")
]
