from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    '''performs other customization for the user'''
    email = models.EmailField(unique=True)


