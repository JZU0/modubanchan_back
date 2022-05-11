"""modubahchan_b URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.menu_list_create,name='menu_list_create'),
    path('<int:menu_pk>/', views.menu_detail_update_delete,name='menu_detail_update_delete'),
    path('<int:menu_pk>/reviews/',views.review_list_create,name='review_list_create'),
    path('<int:menu_pk>/reviews/<int:review_pk>/',views.review_detail_update_delete,name='review_detail_update_delete'),
]
