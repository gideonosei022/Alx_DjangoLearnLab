from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    ExampleForm is used to demonstrate secure form handling.
    It validates and sanitizes user input to prevent SQL injection and XSS.
    """

    class Meta:
        model = Book
        fields = ["title"]

