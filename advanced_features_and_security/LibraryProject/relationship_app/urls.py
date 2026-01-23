from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Auth
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # Role Views
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),

    # Books
    path("books/", views.list_books, name="list_books"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete_book"),

    # Library
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

