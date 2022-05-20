from django.urls import path
from .views import *

app_name="mypage"
urlpatterns = [
   path('',profile_create_detail_update,name='product_list_create'),
]