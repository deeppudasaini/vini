from django.shortcuts import render
from django.http import JsonResponse
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer


@api_view(["GET"])
def CategoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def CategoryDetails(request, pk):
    categories = Category.objects.filter(id=pk)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def CategoryAdd(request):

    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def CategoryUpdate(request, pk):
    updatingCategory = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=updatingCategory, data=request.data)
    if serializer.is_valid():

        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def CategoryDelete(request, pk):
    deletingCategory = Category.objects.get(id=pk)
    deletingCategory.delete()

    return Response("Category Deleted")
