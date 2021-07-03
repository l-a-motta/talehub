# Django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

# Internal imports
from .models import Book, Chapter

# External imports
from django.utils import timezone

# Function to list the five latest books
def index(request):
    latest_books_list = Book.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')[:5]

    context = {'latest_books_list': latest_books_list}
    return render(request, 'catalog/index.html', context)

# Function to show all details of a specific book, including a list of chapters
def details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist as e:
        raise Http404("Error: ", e)

    context = {'book': book}
    return render(request, 'catalog/details.html', context)

# Function to view a specific chapter
def chapter(request, book_id, chapter_id):
    try:
        book = Book.objects.get(pk=book_id)
        chapter = book.chapter_set.get(pk=chapter_id)
    except (Book.DoesNotExist, Chapter.DoesNotExist) as e:
        raise Http404("Error: ", e)

    context = {'chapter': chapter}
    return render(request, 'catalog/chapter.html', context)

# Function to vote in a specific chapter
def vote(request, book_id, chapter_id):
    try:
        book = Book.objects.get(pk=book_id)
        chapter = book.chapter_set.get(pk=chapter_id)
    except (Book.DoesNotExist, Chapter.DoesNotExist) as e:
        raise Http404("Error: ", e)

    try:
        selected_choice = request.POST['choice']
    except (KeyError):
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