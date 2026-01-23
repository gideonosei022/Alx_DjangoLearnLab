from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# ---------------------------
# List all books
# ---------------------------
def book_list(request):
    """
    Display all books in the system.
    Anyone can view this page.
    """
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


# ---------------------------
# Add a new book (requires can_create)
# ---------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    authors = Author.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        Book.objects.create(title=title, author_id=author_id)
        return redirect("book_list")
    return render(request, "bookshelf/add_book.html", {"authors": authors})


# ---------------------------
# Edit a book (requires can_edit)
# ---------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    authors = Author.objects.all()
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author_id = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/edit_book.html", {"book": book, "authors": authors})


# ---------------------------
# Delete a book (requires can_delete)
# ---------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/delete_book.html", {"book": book})
