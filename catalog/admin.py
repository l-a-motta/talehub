# Django imports
from django.contrib import admin

# Internal imports
from .models import Book, Chapter

# * Class for displaying chapters inside of the book entry, in TabularInLine form
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1 # Just one block of new chapter offered by default

# * Class defining the model Book for the admin
class BookAdmin(admin.ModelAdmin):
    # Defining what and how things will be shown in the specific table of a Book
    fieldsets = [
        ('GENERAL BOOK INFO',      {'fields': ['title','long_description','short_description']}),
        ('PUBLISHING INFORMATION', {'fields': ['published_at'], 'classes': ['collapse']}),
    ]
    inlines = [ChapterInline] # Adds the class ChapterInLine to the specific table of a Book
    list_display = ('title', 'created_at', 'published_at', 'was_published_recently') # Defines values shown in the general table
    list_filter = ['created_at', 'published_at'] # Defines filters to be shown in the general table

# * Class defining the model Chapter for the admin
class ChapterAdmin(admin.ModelAdmin):
    # Defining what and how things will be shown in the specific table of a Chapter
    fieldsets = [
        ('GENERAL CHAPTER INFO',      {'fields': ['book', 'name', 'content']}),
        ('PUBLISHING INFORMATION', {'fields': ['published_at'], 'classes': ['collapse']}),
        ('SCORE INFORMATION', {'fields': ['score']}),
    ]
    list_display = ('name', 'book', 'created_at', 'published_at', 'was_published_recently') # Defines values shown in the general table
    list_filter = ['created_at', 'published_at'] # Defines filters to be shown in the general table

# * Registering the models to the admin page
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)