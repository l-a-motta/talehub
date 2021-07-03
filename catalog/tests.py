# Django imports
from django.test import TestCase
from django.utils import timezone

# Internal imports
from .models import Book

# External imports
import datetime


class BookModelTests(TestCase):

    def test_was_created_recently_with_future_book(self):
        """
        was_created_recently() returns False for books whose created_at
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_book = Book(created_at=time)
        self.assertIs(future_book.was_created_recently(), False)

    def test_was_created_recently_with_old_question(self):
        """
        test_was_created_recently() returns False for books whose created_at
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_book = Book(created_at=time)
        self.assertIs(old_book.was_created_recently(), False)

    def test_was_created_recently_with_recent_question(self):
        """
        test_was_created_recently() returns True for books whose created_at
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_book = Book(created_at=time)
        self.assertIs(recent_book.was_created_recently(), True)