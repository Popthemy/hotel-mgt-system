from django.urls import path
from . import views

urlpatterns = [

    path('<int:id>/',views.try_out),
    path('book_rooms/<int:id>/',views.book_room,name='book-room'),
    path('rooms/<int:id>/<int:room_number>/',views.room_detail,name='room-detail'),
]
