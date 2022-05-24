from itertools import product
import profile
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def profile_update(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
