from django.contrib import admin
from .models import Customer, Booking

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('user','username', 'first_name', 'last_name',
                    'email', 'phone_number','address')
    list_display = ('id','username', 'first_name', 'last_name',
                    'email', 'phone_number')
    list_editable = ('first_name', 'last_name','phone_number')
    list_filter = ('created_at','email',)
    search_fields = ('username__icontains', 'first_name__icontains', 'last_name__icontains', 'email')

    


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('id','customer', 'room', 'check_in_date',
                    'check_out_date', 'number_of_guests', 'reserved_date')
    list_editable = ('number_of_guests', 'room')
    list_filter = ('reserved_date', 'check_in_date', 'check_out_date')
    search_fields = ('user__username__icontains', 'room__name__icontains',)

    class Meta:
        fields = "__all__"
