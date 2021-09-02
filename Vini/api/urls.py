from django.urls import path, include
from . import views

from Book import views as book_views
from Category import views as category_views
from Comment import views as comment_views
from Image import views as image_views


urlpatterns = [
    path("", views.index, name="Api"),
    path("books/", book_views.BookList, name="All"),
    path("books/<str:pk>/", book_views.BookDetails, name="Details"),
    path("add-book/", book_views.BookAdd, name="Create"),
    path("edit-book/<str:pk>/", book_views.BookUpdate, name="Update"),
    path("delete-book/<str:pk>/", book_views.BookDelete, name="Delete"),
    path("categories/", category_views.CategoryList, name="All"),
    path("categories/<str:pk>/", category_views.CategoryDetails, name="Details"),
    path("add-category/", category_views.CategoryAdd, name="Create"),
    path("edit-category/<str:pk>/", category_views.CategoryUpdate, name="Update"),
    path("delete-category/<str:pk>/", category_views.CategoryDelete, name="Delete"),
    path("images/", image_views.ImageList, name="All"),
    path("images/<str:pk>/", image_views.ImageDetails, name="Details"),
    path("add-image/", image_views.ImageAdd, name="Create"),
    path("edit-image/<str:pk>/", image_views.ImageUpdate, name="Update"),
    path("delete-image/<str:pk>/", image_views.ImageDelete, name="Delete"),
    path("comments/", comment_views.CommentList, name="All"),
    path("comments/<str:pk>/", comment_views.CommentDetails, name="Details"),
    path("add-comment/", comment_views.CommentAdd, name="Create"),
    path("edit-comment/<str:pk>/", comment_views.CommentUpdate, name="Update"),
    path("delete-comment/<str:pk>/", comment_views.CommentDelete, name="Delete"),
]
