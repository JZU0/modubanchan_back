from django.urls import path
from .views import *

app_name="mypage"
urlpatterns = [
   path('',my_profile,name='profile_name'),
   path('profile_update/',profile_update,name='profile_update'),
   path('<int:id>/',user_profile,name='user_profile'),
   path('user_product/<int:id>',user_product,name='user_product'),
   path('following_list/',following_list,name='following_list'),
   path('follow/<int:id>',follow,name='follow'),
]