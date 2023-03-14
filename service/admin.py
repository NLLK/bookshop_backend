from django.contrib import admin
from service import models

admin.site.register(models.BrowsingHistory)
admin.site.register(models.DeferredBook)
admin.site.register(models.Orders)
admin.site.register(models.Review)
admin.site.register(models.Quotes)
admin.site.register(models.ShoppingCart)
