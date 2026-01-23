import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Example variables (can be replaced in tests)
author_name = "John Doe"
library_name = "Central Library"

# Query all books by a specific author using filter(author=author)
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# List all books in a library using filter(books__in=library.books.all())
library = Library.objects.get(name=library_name)
books_in_library = Book.objects.filter(libraries=library)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

