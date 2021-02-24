from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('allreserves/', views.allreserves, name="allreserves"),
    path('myreserves/', views.myreserves, name="myreserves"),
    # path('myreserves2/', views.myreserves2, name="myreserves2"),
    path('createreserve/<book_id>/', views.createreserve, name="createreserve"),
    path('createcdreserve/<cd_id>/', views.createcdreserve, name="createcdreserve"),
    path('releasereserve/<id>/', views.releasereserve, name="releasereserve"),
    path('releasecdreserve/<id>/', views.releasecdreserve, name="releasecdreserve"),
]