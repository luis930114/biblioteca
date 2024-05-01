# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, PartialBookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return PartialBookSerializer
        return BookSerializer
