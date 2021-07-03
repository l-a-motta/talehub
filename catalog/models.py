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
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    # Function for recent publication of a book
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_at <= now

    def __str__(self):
        return self.title

class Chapter(models.Model):
    # Atributes of a chapter
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=280, default='My Chapter Name')
    content = models.CharField(max_length=1000, default='My Content For The Chapter')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)

    # Function for recent publication of a chapter
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_at <= now

    def __str__(self):
        return self.name