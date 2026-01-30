from django.urls import path, include
from .views import BookList, api_root, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]


