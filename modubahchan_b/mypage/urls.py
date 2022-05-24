from django.urls import path
from .views import *

app_name="mypage"
urlpatterns = [
   path('',profile_update,name='profile_update'),
]