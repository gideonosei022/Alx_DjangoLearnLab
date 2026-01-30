from django.urls import path
from .views import BookList, api_root 

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', api_root, name='api-root'),
]


    