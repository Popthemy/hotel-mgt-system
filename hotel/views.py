from django.shortcuts import render
from django.db.models import Case, When, BooleanField
from .models import Category, Room
# Create your views here.


def categories(request):
    categories = Category.objects.all().annotate(
        is_room=Case(
            When(name__icontains='room', then=True),
            default=False,
            output_field=BooleanField()),
    ).order_by('-is_room')

    context = {'categories': categories}

    # print([ i.is_room for i in categories])
    return render(request, 'hotel/index.html', context)


def category(request, category_id, category_name):

    category = Category.objects.get(id=category_id)
    rooms = category.rooms.all()
    context = {'category': category, 'rooms': rooms}
    # print([room.description for room in rooms ])

    return render(request, 'hotel/single-category.html', context)


# def room_view(request, room_id):
#     room = Room.objects.get(id=id)
