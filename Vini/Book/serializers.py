from rest_framework import serializers
from .models import Book, Book_Category, Book_User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "book_name", "book_author", "book_description", "user_id")


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Category
        fields = ("id", "book_id", "category_id")


class BookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_User
        fields = ("id", "book_id", "user_id")
