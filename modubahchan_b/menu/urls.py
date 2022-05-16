from django.urls import path
from .views import *

app_name="menu"
urlpatterns = [
    path('',product_list_create,name='product_list_create'),
    path('<int:product_pk>/', product_detail_update_delete,name='product_detail_update_delete'),
]