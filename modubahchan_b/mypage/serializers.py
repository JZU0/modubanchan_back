from rest_framework import serializers
from .models import *
from menu.serializers import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['followings']

class UserProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Product
        fields = '__all__'