import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Example variables (you can replace these with any name)
author_name = "John Doe"
library_name = "Central Library"

# Query all books by a specific author
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()

# List all books in a library
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = library.librarian
