from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer



@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Welcome to the API",
        "endpoints": {
            "books": "/api/books/"
        }
    })


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
