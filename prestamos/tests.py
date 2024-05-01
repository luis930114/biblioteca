from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from .models import Book
from .views import BookViewSet
from rest_framework.exceptions import ValidationError


class BookViewSetTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BookViewSet.as_view({'get': 'list', 'post': 'create', 'put':'update', 'delete':'destroy'})
        self.url = reverse('book-list') 

    def test_list_books(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        data = {'title': 'Nuevo libro', 'author': 'Autor', 'isbn': '1234567890', 'genre': 'Ficción'}
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
    
    def test_create_book_with_missing_data(self):
        data = {'author': 'Autor', 'isbn': '1234567890', 'genre': 'Ficción'}
        request = self.factory.post(self.url, data)        
        response = self.view(request)
        self.assertEqual(response.status_code, 400)


    def test_update_book(self):
        data = {'title': 'Nuevo libro', 'author': 'Autor', 'isbn': '1234567890', 'genre': 'Ficción'}
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
        book_id = 1
        detail_url = reverse('book-detail', kwargs={'pk': book_id})
        data = {'title': 'Nuevo título'}  # Datos actualizados del libro
        request = self.factory.put(detail_url, data)
        response = self.view(request, pk=book_id)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        data = {'title': 'Nuevo libro', 'author': 'Autor', 'isbn': '1234567890', 'genre': 'Ficción'}
        request = self.factory.post(self.url, data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
        book_id = dict(response.data)['id']
        detail_url = reverse('book-detail', kwargs={'pk': book_id})
        request = self.factory.delete(detail_url)
        response = self.view(request, pk=book_id)
        self.assertEqual(response.status_code, 204)

    def test_fail_delete_book(self):
        book_id = 1
        detail_url = reverse('book-detail', kwargs={'pk': book_id})
        request = self.factory.delete(detail_url)
        response = self.view(request, pk=book_id)
        self.assertEqual(response.status_code, 404)

