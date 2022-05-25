from django.shortcuts import render, get_object_or_404
from requests import get
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def profile_update(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_profile(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_product(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'GET':
        products = Product.objects.filter(user = user)
        serializer = UserProductSerializer(products, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def following_list(request):
    user = request.user
    # followings = user.profile.followings.all()
    if request.method == 'GET':
        serializer = FollowingSerializer(user.profile)
        return Response(data=serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def follow(request,id):
    user = request.user
    followed_user = get_object_or_404(User, pk = id)
    # followings = user.profile.followings.all()
    is_follower = user.profile in followed_user.profile.followers.all()
    if request.method == 'POST':
        if is_follower:
            user.profile.followings.remove(followed_user.profile)
            serializer = FollowingSerializer(user.profile, data=user.profile.followings.all())
        else:
            user.profile.followings.add(followed_user.profile)
            serializer = FollowingSerializer(user.profile, data=user.profile.followings.all())
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)