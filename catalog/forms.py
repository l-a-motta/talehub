# Django imports
from django import forms
from django.utils import timezone
# Internal imports
# External imports

class BookForm(forms.Form):
    title = forms.CharField(label='Book\'s title', max_length=280)
    published_at = forms.DateTimeField(label='Date for publishing', initial=timezone.now()) # TODO: Fix this so it adds a timezone in a more user-friendly maner