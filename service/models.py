from django.db import models
from books.models import Book
from account.models import User
from assortment.models import Assortment

class Review(models.Model):
    class ReviewStatusChoices(models.IntegerChoices):
        NOT_SEEN = 0
        OK = 1
        DENIED = -1
                
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField(default=0.0)
    moderated = models.SmallIntegerField(choices=ReviewStatusChoices.choices, default=ReviewStatusChoices.NOT_SEEN)
    def __str__(self):
        return f'{self.pk}; {self.ReviewStatusChoices(self.moderated).label}; {self.book.pk}-{self.book.name}; {self.user.pk}-{self.user.last_name};'

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.pk}; {self.assortment.book.name}; {Assortment.AssortmentTypeChoices(self.assortment.assortment_type).label}; {self.number};'

class DeferredBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.pk}; {self.user.pk}-{self.user.last_name}; {self.book.pk}-{self.book.name};'

class Orders(models.Model):
    class OrderStatusChoices(models.IntegerChoices):
        NEW = 0,
        PACKAGED = 50,
        IN_DELIVERY = 70,
        CLOSED = 100,
        CLOSED_REFUND = 101
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    order_status = models.SmallIntegerField(choices=OrderStatusChoices.choices, default=OrderStatusChoices.NEW)
    destination = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.pk}; {self.order_status}; {self.user.pk}-{self.user.last_name}; {self.assortment.book.name}; {AssortmentTypeEnum.toStr(self.assortment.assortment_type)};'

class Quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    moderated = models.SmallIntegerField(default=Review.ReviewStatusChoices.NOT_SEEN)
    def __str__(self):
        return f'{self.pk}; {Review.ReviewStatusChoices(self.moderated).label}; {self.user.pk}-{self.user.last_name}; {self.book.name};'


class BrowsingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.pk} {self.user.pk}-{self.user.last_name}; {self.assortment.book.name};'