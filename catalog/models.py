# Django imports
from django.db import models
from django.utils import timezone

# External imports
import datetime

class Book(models.Model):
    # Atributes of a book
    title = models.CharField(max_length=280, default='My Title')
    long_description =  models.CharField(max_length=560, default='My Long Description')
    short_description =  models.CharField(max_length=280, default='My Short Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Function for recent creation of a book
    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    def __str__(self):
        return self.title

class Chapter(models.Model):
    # Atributes of a chapter
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=280, default='My Chapter Name')
    content = models.CharField(max_length=1000, default='My Content For The Chapter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name