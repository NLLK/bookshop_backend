from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assortment
from books.models import Book, Book_genre
from service.models import Review, ReviewStatusEnum
from django.db.models import Max, Subquery, Avg

class GetAssortmentListView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    @staticmethod
    def create_content_obj(assortment, authors, genres, assortment_types, rating):
        return {
            'book_id': assortment.book.id,
            'title': assortment.book.name,
            'authors': authors,
            'genres': genres,
            'publisher': assortment.book.publisher.name,
            'series': assortment.book.series.name,
            'publish_year': assortment.book.publish_year,
            'age_restriction': assortment.book.age_restriction,
            'img_link': assortment.book.img_link.name,
            # 'page_number': assortment.page_number,
            # 'audio_length_min': assortment.audio_length_min,
            #'price': assortment.price,
            'number': assortment.number,
            'rating': rating,
            #'links': [link.url for link in assortment.links.all()],
            'assortment_types': [assortment_type.name for assortment_type in assortment_types]
        }

    def get(self, request, format=None):
        #filters: available, genres, type, price, year, rating
        assortment_list = Assortment.objects.filter(available = True).select_related('book').prefetch_related('book__authors', 'book__genres')

        content = []
        assortment_types = {}
        ratings = {}

        params = request.query_params

        if 'available' in params:
            assortment_list = assortment_list.filter(available=params['available'])
        if 'genres' in params:
            genres = params['genres'].split(',')
            assortment_list = assortment_list.filter(book__genres__id__in=genres).distinct()
        if 'type' in params:
            types = params['type'].split(',')
            assortment_list = assortment_list.filter(assortment_type__id__in=types)
        # if 'price' in params:
        #     price = params['price'].split('-')
        #     if len(price) == 1:
        #         assortment_list = assortment_list.filter(price=price[0])
        #     elif len(price) == 2:
        #         assortment_list = assortment_list.filter(price__range=(price[0], price[1]))
        if 'publish_year' in params:
            year = params['publish_year'].split('-')
            if len(year) == 1:
                assortment_list = assortment_list.filter(book__publish_year=year[0])
            elif len(year) == 2:
                assortment_list = assortment_list.filter(book__publish_year__range=(year[0], year[1]))
                #rating = Review.objects.filter(book__pk = book.pk, moderated = ReviewStatusEnum.OK).aggregate(Avg('rating'))['rating__avg']    

        for assortment in assortment_list:
            book_id = assortment.book.id
            if book_id not in assortment_types:
                assortment_types[book_id] = []
            assortment_types[book_id].append(assortment.assortment_type)

        for assortment in assortment_list:
            book_id = assortment.book.id
            if book_id not in [x['book_id'] for x in content]:
                book = assortment.book
                authors = [f"{author.firstname} {author.lastname}" for author in book.authors.all()]
                genres = [genre.name for genre in book.genres.all()]

                rating_avg = Review.objects.filter(book__pk = book.pk, moderated = ReviewStatusEnum.OK).aggregate(Avg('rating'))['rating__avg']
                
                rating_flag = True

                if 'rating' in params:
                    rating_flag = False
                    rating_range = params['rating'].split('-')
                    if len(rating_range) == 1:
                        try:
                            rating = float(rating_range[0])
                            if rating_avg >= rating:
                                rating_flag = True
                        except ValueError:
                            pass
                    elif len(rating_range) == 2:
                        try:
                            rating_min = float(rating_range[0])
                            rating_max = float(rating_range[1])
                            if rating_max >= rating_avg and rating_min <= rating_avg :
                                rating_flag = True

                        except ValueError:
                            pass
                if rating_flag:
                    content.append(GetAssortmentListView.create_content_obj(assortment, authors, genres, assortment_types[book.id], rating_avg))
            
        return Response(content)
# Create your views here.