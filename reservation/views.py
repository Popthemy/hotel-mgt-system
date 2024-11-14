from django.shortcuts import render,HttpResponse
from hotel.models import Room
from .models import Booking
from .my_utils import check_clashes
from datetime import date
# Create your views here.

def try_out(request,id):

  res = check_clashes(model=Booking,room=id,start=date(2021,10,1), end=date(2024,11,19))

  return HttpResponse(res)


def room_detail(request,id,room_number):
  '''This view provides details about the room and its bookings'''

  bookings = Booking.objects.filter(room=id,room__room_number=room_number)
  room = Room.objects.get(id=id)

  context = {'bookings':bookings,'room':room}
    # templates\reservation\single_room.html
  return render(request, r'reservation\single_room.html',context)