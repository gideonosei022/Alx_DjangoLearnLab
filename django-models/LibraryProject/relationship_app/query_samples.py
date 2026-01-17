import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = author.books.all()

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = library.librarian
