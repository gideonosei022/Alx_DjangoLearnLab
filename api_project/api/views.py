from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Welcome to the API",
        "endpoints": {
            "books": "/api/books/"
        }
    })
