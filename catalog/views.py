# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# Internal imports
from .models import Book, Chapter

# Create your views here.

def index(request):
    latest_books_list = Book.objects.order_by('-created_at')[:5]
    context = {'latest_books_list': latest_books_list}
    return render(request, 'catalog/index.html', context)

def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)

def chapters(request, book_id):
    response = "You're looking at the chapters of book %s."
    return HttpResponse(response % book_id)