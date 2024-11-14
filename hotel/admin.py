from django.contrib import admin
from .models import Room, Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'max_occupants')
    list_display = ('id', 'name', 'max_occupants')
    list_filter = ('name', 'max_occupants')
    search_fields = ('name', 'max_occupants')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    '''room_number category ,description,is_available ,bed_type,floor,image_url'''

    fields = ('room_number', 'category', 'is_available', 'floor', 'bed_type',
              'price_per_night', 'image_url',  'description')
    list_editable = ('is_available',)
    list_display = ('id','room_number', 'is_available', 'price_per_night', 'floor')
    list_filter = ('floor', 'is_available')
    search_fields = ('room_number', 'floor', 'category')
