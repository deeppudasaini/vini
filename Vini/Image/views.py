from django.shortcuts import render
from django.http import JsonResponse
from .models import Image
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer


@api_view(["GET"])
def ImageList(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def ImageDetails(request, pk):
    images = Image.objects.filter(id=pk)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def ImageAdd(request):

    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def ImageUpdate(request, pk):
    updatingImage = Image.objects.get(id=pk)
    serializer = ImageSerializer(instance=updatingImage, data=request.data)
    if serializer.is_valid():

        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def ImageDelete(request, pk):
    deletingImage = Image.objects.get(id=pk)
    deletingImage.delete()

    return Response("Image Deleted")
