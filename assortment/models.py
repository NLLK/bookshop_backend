from django.db import models
from books.models import Book
import json

def user_directory_path(instance, filename):
    audio = 'audio'
    text = 'text'
    pre = 'books_resources/'

    if any([x in filename for x in ['.mp3', '.aac', '.ogg', '.m4b', '.wav']]):
        pre += audio

    if any([x in filename for x in ['.epub', '.pdf', '.mobi', '.azw', '.djvu']]):
        pre += text

    return f'{pre}/{filename}'

class AssortmentLink(models.Model):
    class AssortmentLinkChoices(models.IntegerChoices):
        PREVIEW = 0,
        FULL = 1,
    link_type = models.SmallIntegerField(default=AssortmentLinkChoices.PREVIEW, choices=AssortmentLinkChoices.choices)
    row_link = models.FileField(upload_to = user_directory_path)
    def __str__(self):
        return f'{self.pk}; {self.AssortmentLinkChoices(self.link_type).label}; {self.row_link}'

class Assortment(models.Model):

    class AssortmentTypeChoices(models.IntegerChoices):
        EBOOK = 1
        PAPER = 2
        AUDIO = 3

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    assortment_type = models.SmallIntegerField(default=AssortmentTypeChoices.PAPER, choices=AssortmentTypeChoices.choices)
    available = models.BooleanField()
    page_number = models.IntegerField(blank=True)
    audio_length_min = models.IntegerField(blank=True, default=-1)
    price = models.FloatField(blank=True)
    number = models.IntegerField(blank=True)
    links = models.ManyToManyField(AssortmentLink, blank=True)

    def __str__(self):
        return f'{self.pk}; {self.book.name}; {self.AssortmentTypeChoices(self.assortment_type).label}; {self.available}'

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
