# Django imports
from django.contrib import admin

# Internal imports
from .models import Book, Chapter

# Register your models here.

admin.site.register(Book)
admin.site.register(Chapter)