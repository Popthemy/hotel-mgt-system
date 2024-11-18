from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.conf import settings
from hotel.models import Room
from .my_utils import check_clashes
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField(help_text='when will you will arrive at our hotel..')
    check_out_date = models.DateField(help_text='when you will vacate the room..')
    number_of_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])
    reserved_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.customer.username} for Room {self.room}"

    def clean(self):
        if self.check_out_date < self.check_in_date:
            raise ValidationError(
                'Check-out date must be after check-in date.')

    class Meta:
        # Prevent double booking of the same room
        unique_together = ('customer', 'room', 'check_in_date', 'check_out_date')

    def save(self,*args, **kwargs) -> None:
        print('$$$$$$$ CHECKING CLASHES FROM MODELS SAVE  $$$$$')
        check_clashes(Booking,room=self.room,start=self.check_in_date, end=self.check_out_date)
        super().save(*args, **kwargs)
