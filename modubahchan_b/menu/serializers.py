from asyncore import read
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class ProductListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Product
        fields = '__all__'

class FollowingProductListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Product
        fields = '__all__'