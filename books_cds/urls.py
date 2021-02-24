from django.urls import path
from . import views

app_name = 'books_cds'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('addbook/', views.book_add, name='book_add'),
    path('addcd/', views.cd_add, name='cd_add'),

    path('viewbook/<book_id>/', views.book_detail, name='book_detail'),
    path('viewcd/<cd_id>', views.cd_detail, name='cd_detail'),

    path('editbook/<book_id>/', views.book_edit, name='book_edit'),
    path('editcd/<cd_id>', views.cd_edit,  name='cd_edit'),
    
    path('deletebook/<book_id>/', views.book_delete, name='book_delete'),
    path('deletecd/<cd_id>', views.cd_delete, name='cd_delete'),
]