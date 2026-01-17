from django.shortcuts import render

# Create your views here. 

# Function-based views to handle requests related to Book model

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    return HttpResponse(output, content_type="text/plain")

# class-based views to handle requests related to Author model
from django.views.generic import DetailView
from .models import Library

# Class-based view: Show details of a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
