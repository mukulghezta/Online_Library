from django.contrib import admin
from .models import Book, CD

class BookAdmin(admin.ModelAdmin):
    list_display=['book_id','book_name','book_author','book_language', 'book_quantity']

admin.site.register(Book, BookAdmin)

class CDAdmin(admin.ModelAdmin):
    list_display=['cd_id','cd_name','cd_artist','cd_language', 'cd_quantity']

admin.site.register(CD, CDAdmin)