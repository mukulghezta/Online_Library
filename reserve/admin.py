from django.contrib import admin
from .models import BookReserve, CDReserve

class BookReserveAdmin(admin.ModelAdmin):
    list_display=['user_id','book_id','reserve_date', 'due_date']

admin.site.register(BookReserve, BookReserveAdmin)


class CDReserveAdmin(admin.ModelAdmin):
    list_display=['user_id','cd_id','reserve_date', 'due_date']

admin.site.register(CDReserve, CDReserveAdmin)