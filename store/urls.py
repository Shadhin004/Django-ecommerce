from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('shop/', views.shop, name='shop'),
    path('shop/product/<int:myid>', views.product, name='product'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('register/', views.register, name= 'register'),

]