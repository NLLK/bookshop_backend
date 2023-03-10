from django.db import models
from books.models import Book
from account.models import User
from assortment.models import AssortmentType, Assortment
#quotes, review, deferred books, shopping cart, orders, browsing history

class ReviewStatusEnum():
    NOT_SEEN = 0
    OK = 1
    DENIED = -1

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField(blank=True)
    moderated = models.IntegerField()

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)

class DeferredBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class OrderStatus(models.Model):
    name = models.CharField(max_length=255)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)

class Quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()

class BrowsingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)