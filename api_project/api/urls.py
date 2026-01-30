from django.urls import path
from .views import book_list, api_root 

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('', api_root, name='api-root'),
]


    