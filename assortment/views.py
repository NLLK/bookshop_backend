from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assortment
from books.models import Book, Book_genre
from django.db.models import Max, Subquery

class GetAssortmentListView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def create_content_obj(assortment, authors, genres):
        return {
            'book_name': assortment.book.name,
            'authors': authors,
            'genres': genres
        }

    def get(self, request, format=None):
        assortment_list = Assortment.objects.filter(
            id__in=Subquery(
                Assortment.objects.values('book_id').annotate(max_id=Max('id')).values('max_id')
            )
        ).select_related('book').prefetch_related('book__authors', 'book__genres')
        content = []
        for assortment in assortment_list:
            book = assortment.book
            authors = [f"{author.firstname} {author.lastname}" for author in book.authors.all()]
            genres = [genre.name for genre in book.genres.all()]
            # print(f"Book name: {book.name}")
            # print(f"Authors: {authors}")
            # print(f"Genres: {genres}")
            content.append(GetAssortmentListView.create_content_obj(assortment,authors,genres))

        

        return Response(content)
# Create your views here.