from django.contrib import admin
from assortment import models

admin.site.register(models.Assortment)
admin.site.register(models.AssortmentLink)
admin.site.register(models.AssortmentType)

