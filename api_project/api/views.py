from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.

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
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


    
# New ViewSet for full CRUD
