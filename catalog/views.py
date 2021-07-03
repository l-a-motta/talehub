# Django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Internal imports
from .models import Book, Chapter

# Function to list all books
def index(request):
    latest_books_list = Book.objects.order_by('-created_at')[:5]
    context = {'latest_books_list': latest_books_list}
    return render(request, 'catalog/index.html', context)

# Function to show all details of a specific book, including a list of chapters
def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'catalog/details.html', context)

# Function to view a specific chapter
def chapter(request, book_id, chapter_id):
    book = get_object_or_404(Book, pk=book_id)
    chapter = book.chapter_set.get(pk=chapter_id)
    context = {'chapter': chapter}
    return render(request, 'catalog/chapter.html', context)

# Function to vote in a specific chapter
def vote(request, book_id, chapter_id):
    book = get_object_or_404(Book, pk=book_id)
    chapter = book.chapter_set.get(pk=chapter_id)

    try:
        selected_choice = request.POST['choice']
    except (KeyError, Chapter.DoesNotExist):
        # Redisplay the question voting form because there was no vote.
        context = {
            'chapter': chapter,
            'error_message': "You didn't vote.",
        }
        return render(request, 'catalog/chapter.html', context)
    else:
        # Check for the selected vote, 1 for positive and 0 for negative vote
        if selected_choice == "1":
            chapter.votes += 1
        elif selected_choice == "0":
            chapter.votes -= 1
        chapter.save() # Look into F(), at Django docs. Better performance

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('catalog:details', args=(book.id,)))