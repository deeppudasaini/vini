from django.db import models

# Create your models here.
class Comment(models.Model):
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    book_id = models.ForeignKey(
        "Book.Book", on_delete=models.CASCADE, null=True, blank=True
    )
    user_id = models.ForeignKey(
        "User.User", on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(max_length=1000)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
