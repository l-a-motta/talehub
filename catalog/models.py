# Django imports
from django.db import models
from django.utils import timezone

# External imports
import datetime

# Create your models here.

class Book(models.Model):
    # Atributes of a book
    title = models.CharField(max_length=280)
    long_description =  models.CharField(max_length=560)
    short_description =  models.CharField(max_length=280)
    created_at = models.DateTimeField('date of creation')
    published_at = models.DateTimeField('date published')

    # Function for recent creation of a book
    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

    # Function for recent publication of a book
    def was_published_recently(self):
        return self.published_at >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=280)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.name