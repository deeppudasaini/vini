from django.db import models

# Create your models here.
class Book(models.Model):
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name


class Book_User(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_id


class Book_Category(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category.Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_id
