from telnetlib import STATUS
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET','POST'])
def cart_list_create(request):
    if request.method=='GET':
        carts = Cart.objects.all()
        serializer = CartListSerializer(carts, many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = CartListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=STATUS.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def cart_update_delete(request,cart_pk):
    cart = get_object_or_404(Cart, pk=cart_pk)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cart.delete()
        data={'cart_pk':cart_pk}
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CartSerializer(instance=cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return(serializer.data)
