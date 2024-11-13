from django.db import models
from django.conf import settings
from hotel.models import Room

# Create your models here.


# class Customer(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Booking(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     number_of_guests = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
      # updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Booking by {self.user.username} for Room {self.room.number}"

#     class Meta:
#         unique_together = ('user', 'room', 'start_date', 'end_date')  # Prevent double booking of the same room
