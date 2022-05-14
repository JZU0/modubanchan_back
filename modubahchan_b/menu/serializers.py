from asyncore import read
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','name','category', 'description','createDate','updateDate','feedText', 'category','picture')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','category', 'description','createDate','updateDate','feedText', 'category','picture')

