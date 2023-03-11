from django.contrib import admin
from books import models

admin.site.register(models.Book)
admin.site.register(models.Series)
admin.site.register(models.Publisher)
admin.site.register(models.Book_author)
admin.site.register(models.Book_genre)

