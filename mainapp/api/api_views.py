from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter

from .serializers import CategorySerializer, CustomerSerializer, SmartphoneSerializer, NotebookSerializer
from ..models import Category, Customer

class CategoryPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('objects', data)
        ]))

class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):

    pagination_class = CategoryPagination
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

class CategoryDetailAPIView(RetrieveAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

class SmartphoneListAPIView(ListAPIView):

    serializer_class = SmartphoneSerializer
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class NotebookListAPIView(ListAPIView):

    serializer_class = NotebookSerializer

class SmartphoneDetailAPIView(RetrieveAPIView):

    serializer_class = SmartphoneSerializer
    lookup_field = 'id'

class NotebookDetailView(RetrieveAPIView):

    serializer_class = NotebookSerializer
    lookup_field = 'id'

class CustomerListAPIView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
