from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from hotel.models import Room
from .models import Booking
from .my_utils import check_clashes
from datetime import date
from .forms import BookingForm
# Create your views here.


def try_out(request, id):

    res = check_clashes(model=Booking, room=id, start=date(
        2021, 10, 1), end=date(2024, 11, 19))

    return HttpResponse(res)


def room_detail(request, id, room_number):
    '''This view provides details about the room and its bookings'''

    bookings = Booking.objects.filter(room=id, room__room_number=room_number)
    room = Room.objects.get(id=id)

    context = {'bookings': bookings, 'room': room}
    # templates\reservation\single_room.html
    return render(request, r'reservation\single_room.html', context)


def book_room(request, id):
    room = Room.objects.get(id=id)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        print('This is the room number:',request.POST.get('room'))

        if form.is_valid():
            # form.save()

            message = 'Trying checking for availability!'
            messages.info(request, message)

            return redirect('room_detail', id, room.room_number)

    context = {'room': room, 'form': form}
    return render(request, 'reservation/booking_form.html', context)
