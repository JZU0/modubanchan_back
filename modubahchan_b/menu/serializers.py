from asyncore import read
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','content','menu')
        read_only_fields=('menu')
        
class MenuListSerializer(serializers.ModelSerializer):

    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count',read_only=True)

    class Meta:
        model = Menu
        fields = ('id','name','description','created_at','updated_at','review_set', 'review_count')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name','description','created_at','updated_at')

