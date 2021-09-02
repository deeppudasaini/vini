from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return JsonResponse(
        {
            "message": "Api Home Page",
            "end-points": {
                "books": {
                    "get": "books/",
                    "post": "add-book/",
                    "put": "edit-book/",
                    "delete": "delete-book/",
                },
                "categories": {
                    "get": "categories/",
                    "post": "add-category/",
                    "put": "edit-category/",
                    "delete": "delete-category/",
                },
                "comments": {
                    "get": "comments/",
                    "post": "add-comment/",
                    "put": "edit-comment/",
                    "delete": "delete-comment/",
                },
                "images": {
                    "get": "images/",
                    "post": "add-image/",
                    "put": "edit-image/",
                    "delete": "delete-image/",
                },
            },
        }
    )
