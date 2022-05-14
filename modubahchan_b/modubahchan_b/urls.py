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
from cart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.product_list_create,name='product_list_create'),
    path('<int:product_pk>/', views.product_detail_update_delete,name='product_detail_update_delete'),
    path('cart/',views.cart_list_create,name='cart_list_create'),
    path('cart/<int:cart_pk>/',views.cart_update_delete,name='cart_update_delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
