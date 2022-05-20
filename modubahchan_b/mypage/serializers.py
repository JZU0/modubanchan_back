from rest_framework import serializers
from menu.serializers import ProductSerializer
from .models import *
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    product_set = ProductSerializer(many=True, read_only = True)
    product_count = serializers.IntegerField(source='product_set.count', read_only=True)
    class Meta:
        model = Profile
        fields = ('id','user', 'nickname','memo','product_set', 'product_count')