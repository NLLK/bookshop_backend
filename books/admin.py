from django.contrib import admin
from books import models

admin.site.register(models.Book)
admin.site.register(models.Series)
admin.site.register(models.Publisher)
admin.site.register(models.Book_genre_list)
admin.site.register(models.Book_genre)

