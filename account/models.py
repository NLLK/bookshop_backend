from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

from datetime import date

class User_permissions_enum:
    temp_user = -1
    guest = 0
    user = 1 
    admin = 2 
    director = 3
    
class City(models.Model):
    name = models.CharField(max_length=150)

class User(AbstractUser):
    permissions = models.SmallIntegerField(
        validators=[MaxValueValidator(User_permissions_enum.director), MinValueValidator(User_permissions_enum.temp_user)],
        default=User_permissions_enum.guest
    )

    date_of_birth = models.DateField(default=None, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
