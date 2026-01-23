from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    BookForm is used to safely validate and sanitize user input.
    Using Django forms helps prevent SQL injection and XSS attacks.
    """

    class Meta:
        model = Book
        fields = ["title"]
