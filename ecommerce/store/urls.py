from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('logout/', views.logout_user, name="logout"),
] 