from django.db import models
from books_cds.models import Book, CD
from django.contrib.auth.models import User


class BookReserve(models.Model):
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)
    reserve_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=False)
    days_for_expiry = models.IntegerField(default=14)

    def __str__(self):
        return str(self.user_id)


class CDReserve(models.Model):
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    cd_id = models.ForeignKey(CD, default=None, on_delete=models.CASCADE)
    reserve_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return str(self.user_id)