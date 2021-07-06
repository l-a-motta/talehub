# Django imports
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# Internal imports
from .models import Book, Chapter
# External imports
import datetime

# Function for creating a book and publishing it within a certain time offset in days
def create_book(title, long_description, short_description, days):
    """
    Create a book with the given data, but sets the published date with the
    given number of `days` offset to now (negative for books published
    in the past, positive for books that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Book.objects.create(title=title, long_description=long_description, short_description=short_description, published_at=time)

# Function for creating a chapter and publishing it within a certain time offset in days
def create_chapter(book, name, content, score, days):
    """
    Create a chapter with the given data, but sets the published date with the
    given number of `days` offset to now (negative for chapters published
    in the past, positive for chapters that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Chapter.objects.create(book=book, name=name, content=content, score=score, published_at=time)

# Tests for the model of a book
class BookModelTests(TestCase):

    def test_was_published_recently_with_future_book(self):
        """
        was_published_recently() returns False for books whose published_at
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_book = Book(published_at=time)
        self.assertIs(future_book.was_published_recently(), False)

    def test_was_published_recently_with_old_book(self):
        """
        test_was_published_recently() returns False for books whose published_at
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_book = Book(published_at=time)
        self.assertIs(old_book.was_published_recently(), False)

    def test_was_published_recently_with_recent_book(self):
        """
        test_was_published_recently() returns True for books whose published_at
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_book = Book(published_at=time)
        self.assertIs(recent_book.was_published_recently(), True)

# Tests for the view of the index, with many books
class BookIndexViewTests(TestCase):
    def test_no_books(self):
        """
        If no books exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No books are available.")
        self.assertQuerysetEqual(response.context['latest_books_list'], [])

    def test_past_book(self):
        """
        books with a published_at in the past are displayed on the
        index page.
        """
        book = create_book(title="Past book.", long_description="Default loooong description.", short_description="Default short desc.", days=-30)
        response = self.client.get(reverse('catalog:index'))
        self.assertQuerysetEqual(response.context['latest_books_list'],[book],)

    def test_future_book(self):
        """
        books with a published_at in the future aren't displayed on
        the index page.
        """
        create_book(title="Future book.", long_description="Default loooong description.", short_description="Default short desc.", days=30)
        response = self.client.get(reverse('catalog:index'))
        self.assertContains(response, "No books are available.")
        self.assertQuerysetEqual(response.context['latest_books_list'], [])

    def test_future_book_and_past_book(self):
        """
        Even if both past and future books exist, only past books
        are displayed.
        """
        book = create_book(title="Past book.", long_description="Default loooong description.", short_description="Default short desc.", days=-30)
        create_book(title="Future book.", long_description="Default loooong description.", short_description="Default short desc.", days=30)
        response = self.client.get(reverse('catalog:index'))
        self.assertQuerysetEqual(response.context['latest_books_list'],[book],)

    def test_two_past_books(self):
        """
        The books index page may display multiple books.
        """
        book1 = create_book(title="Reeeally old book 2.", long_description="Default loooong description.", short_description="Default short desc.", days=-30)
        book2 = create_book(title="Old book 1.", long_description="Default loooong description.", short_description="Default short desc.", days=-5)
        response = self.client.get(reverse('catalog:index'))
        self.assertQuerysetEqual(response.context['latest_books_list'],[book2, book1],)

    def test_book_without_chapters(self):
        """
        A book with no published chapters should not show any chapters
        """
        book1 = create_book(title="Book without chapter.", long_description="Default loooong description.", short_description="Default short desc.", days=-5)
        chapter1 = create_chapter(book=book1, name="Unpublished chapter", content="Looots of content", score=0, days=5)

        response = self.client.get(reverse('catalog:details', args=(str(book1.id))))

        self.assertIn(response.context['book'].title, book1.title) # ? Weird test, not like the other assertQuerysetEqual, but technically it should have the title so it's ok?
        self.assertQuerysetEqual(response.context['chapters'],[],)