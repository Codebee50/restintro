from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.


# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     book_serializer = BookSerializer(books, many=True)
#     return Response(book_serializer.data)


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data)
    
    def post(self, request):
        name = request.data.get('name')
        author = request.data.get('author')
        number_of_pages = request.data.get('number_of_pages')
        number_of_chapters = request.data.get('number_of_chapters')
        image = request.data.get('book_cover')
        
        
        # #Books.objects.creates stores a new record and returns the created record as a python object
        book = Book.objects.create(
            name=name, author=author, 
            number_of_pages=number_of_pages, 
            number_of_chapters=number_of_chapters,
            book_cover=image)
        book_serializer = BookSerializer(book)
        return Response({
            'message': "Book created successfully", 
            "book": book_serializer.data
            })
        
    

class BookListGeneric(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
