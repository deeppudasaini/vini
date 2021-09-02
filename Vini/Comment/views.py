from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer


@api_view(["GET"])
def CommentList(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def CommentDetails(request, pk):
    comments = Comment.objects.filter(id=pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def CommentAdd(request):

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def CommentUpdate(request, pk):
    updatingComment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=updatingComment, data=request.data)
    if serializer.is_valid():

        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def CommentDelete(request, pk):
    deletingComment = Comment.objects.get(id=pk)
    deletingComment.delete()

    return Response("Comment Deleted")
