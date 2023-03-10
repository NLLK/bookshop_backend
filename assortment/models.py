from django.db import models
from books.models import Book

class AssortmentType(models.Model):
    name = models.CharField(max_length=255)

class Assortment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    assortment_type = models.ForeignKey(AssortmentType, on_delete=models.CASCADE)
    available = models.BooleanField()
    page_number = models.IntegerField(blank=True)
    audio_length_min = models.IntegerField(blank=True, default=-1)
    price = models.FloatField(blank=True)
    number = models.IntegerField(blank=True)

def user_directory_path(instance, filename):
    audio = 'audio'
    text = 'text'
    pre = 'books_resources/'

    if any([x in filename for x in ['.mp3', '.aac', '.ogg', '.m4b', '.wav']]):
        pre += audio

    if any([x in filename for x in ['.epub', '.pdf', '.mobi', '.azw', '.djvu']]):
        pre += text

    return f'{pre}/{filename}'

class link_types_enum:
  preview = 0
  full = 1


class AssortmentLinks(models.Model):
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    link_type = models.SmallIntegerField()
    row_link = models.FileField(upload_to = user_directory_path)
