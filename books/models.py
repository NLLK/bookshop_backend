from django.db import models
from django.conf import settings

class Publisher(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.pk}; {self.name}'

class Series(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.pk}; {self.name}'

def user_directory_path(instance, filename):
    return 'images/books/'+f'{filename}'

class Book_genre(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.pk}; {self.name}'

class Book_author(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.pk}; {self.lastname} {self.firstname}'

class Book(models.Model):
    name = models.CharField(max_length=150)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True)
    publish_year = models.SmallIntegerField(blank=False)
    age_restriction = models.SmallIntegerField(blank=True)
    description = models.TextField(blank=True)
    img_link = models.FileField(upload_to = user_directory_path, blank=True)
    genres = models.ManyToManyField(Book_genre)
    authors = models.ManyToManyField(Book_author)
    def __str__(self):
        return f'{self.pk}; {self.name} {self.publisher.name}'