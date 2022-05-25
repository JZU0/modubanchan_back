from django.urls import path
from .views import *

app_name="mypage"
urlpatterns = [
   path('',my_profile,name='profile_name'),
   path('profile_update/',profile_update,name='profile_update'),
   path('user_profile/<int:id>',user_profile,name='user_profile'),
   path('user_product/<int:id>',user_product,name='user_product'),
]