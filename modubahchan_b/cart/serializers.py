from itertools import product
from rest_framework import serializers
from .models import *
from menu.models import Product

class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'productList', 'productNum')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'productList', 'productNum')