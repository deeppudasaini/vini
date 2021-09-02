from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer


@api_view(["GET"])
def BookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def BookDetails(request, pk):
    books = Book.objects.filter(id=pk)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def BookAdd(request):

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def BookUpdate(request, pk):
    updatingBook = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=updatingBook, data=request.data)
    if serializer.is_valid():

        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def BookDelete(request, pk):
    deletingBook = Book.objects.get(id=pk)
    deletingBook.delete()

    return Response("Book Deleted")
