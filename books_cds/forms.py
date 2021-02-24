from django import forms
from .models import Book, CD

class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_id', 'book_name', 'book_author', 'book_language', 'book_quantity']

class CreateCD(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['cd_id', 'cd_name', 'cd_artist', 'cd_language', 'cd_quantity']