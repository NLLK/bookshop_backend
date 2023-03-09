from django.contrib import admin
from account import models

admin.site.register(models.User)
admin.site.register(models.City)

# Register your models here.
