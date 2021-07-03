# Django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Internal imports
from .models import Book, Chapter

# Create your views here.

def index(request):
    latest_books_list = Book.objects.order_by('-created_at')[:5]
    context = {'latest_books_list': latest_books_list}
    return render(request, 'catalog/index.html', context)

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'catalog/details.html', context)

def chapter(request, book_id, chapter_id):
    book = get_object_or_404(Book, pk=book_id)
    chapter = book.chapter_set.get(pk=chapter_id)
    context = {'chapter': chapter}
    return render(request, 'catalog/chapter.html', context)