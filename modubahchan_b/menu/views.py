from telnetlib import STATUS
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
# Create your views here.

@api_view(['GET','POST'])
def menu_list_create(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuListSerializer(menus, many=True)
        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = MenuListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=STATUS.HTTP_201_CREATED)
    
@api_view(['GET','DELETE','PUT'])
def menu_detail_update_delete(request,menu_pk):
    menu = get_object_or_404(Menu, pk=menu_pk)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        menu.delete()
        data={
            'menu':menu_pk
        }
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MenuSerializer(instance=menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET','POST'])
def review_list_create(request,menu_pk):
    menu = get_object_or_404(Menu,pk=menu_pk)

    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(menu=menu)
        return Response(serializer.data, status=STATUS.HTTP_201_CREATED)
    elif request.method=='GET':
        reviews = menu.review_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail_update_delete(request,menu_pk,review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method=='GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response({'review_pk':review_pk},status=STATUS.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=STATUS.HTTP_200_OK)