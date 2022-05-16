from django.urls import path
from .views import *

app_name="cart"
urlpatterns = [
    path('cart/',cart_list_create,name='cart_list_create'),
    path('cart/<int:cart_pk>/',cart_update_delete,name='cart_update_delete'),
]