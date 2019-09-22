from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AllAuthors(ListAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorView(APIView):

    def get(self, request, pk, format=None):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_200_OK)


class AllBooks(ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):

    def get(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)
