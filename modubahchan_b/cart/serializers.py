from itertools import product
from rest_framework import serializers
from .models import *
from menu.models import Product

class CartListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Cart
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Cart
        fields = '__all__'