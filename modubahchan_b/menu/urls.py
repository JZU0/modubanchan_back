from django.urls import path
from .views import *

app_name="menu"
urlpatterns = [
    path('',product_list_create,name='product_list_create'),
    path('<int:product_pk>/', product_detail_update_delete,name='product_detail_update_delete'),
    path('followingProducts/', following_product_list, name='following_product_list'),
    path('search/<str:word>', search_products, name='search_products'),
]