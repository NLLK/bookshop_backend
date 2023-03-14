from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

from datetime import date
    
class City(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.pk}; {self.name}'

class User(AbstractUser):
    class UserPermissionsChoices(models.IntegerChoices):
        temp_user = -1
        guest = 0
        user = 1 
        admin = 2 
        director = 3

    permissions = models.SmallIntegerField(default=UserPermissionsChoices.guest, choices=UserPermissionsChoices.choices)

    date_of_birth = models.DateField(default=None, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}; {self.UserPermissionsChoices(self.permissions).label}; {self.last_name} - {self.email}'
