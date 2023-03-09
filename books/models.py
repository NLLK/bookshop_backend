from django.db import models
from django.conf import settings

class Publisher(models.Model):
    name = models.CharField(max_length=150)

class Series(models.Model):
    name = models.CharField(max_length=150)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return settings.MEDIA_ROOT+'/books/images/'+f'{instance.id}_{filename}'
    return 'images/books/'+f'{filename}'

class Book(models.Model):
    name = models.CharField(max_length=150)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True)
    publish_year = models.SmallIntegerField(blank=False)
    age_restricion = models.SmallIntegerField(blank=True)
    description = models.TextField(blank=True)
    img_link = models.FileField(upload_to = user_directory_path, blank=True)

class Book_genre(models.Model):
    name = models.CharField(max_length=150)

class Book_genre_list(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_genre = models.ForeignKey(Book_genre, on_delete=models.CASCADE)