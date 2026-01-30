from django.urls import path, include
from .views import BookList, api_root, BookViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token),
]

