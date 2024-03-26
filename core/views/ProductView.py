from django_filters.rest_framework import DjangoFilterBackend
from core.models.Product import Product
from core.serializers.ProductSerializer import ProductSerializer
from core.pagination.BasicPagination import CustomPagination
from rest_framework import filters
from rest_framework import generics


'''
 - documentation: https://www.django-rest-framework.org/api-guide/filtering/
 - filter example: http://example.com/api/products/?category=clothing&in_stock=True 
 - search example: http://example.com/api/users/?search=russell 
 - pagination: GET https://api.example.org/accounts/?limit=100&offset=400
'''


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    pagination_class = CustomPagination


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
