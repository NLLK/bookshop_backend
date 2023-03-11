from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assortment

class GetAssortmentListView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        objects = Assortment.objects.values(
            'id', 'book__name', 'book__publisher__name', 'book__series__name',
            'book__publish_year', 'book__age_restriction','price', 
            'book__authors__firstname', 'book__authors__lastname',
            'book__genres')
        content = objects
        
        return Response(content)
# Create your views here.