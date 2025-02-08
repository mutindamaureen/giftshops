from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer
from PIL import Image
from io import BytesIO
from django.http import Http404
from rest_framework import status
from rest_framework import generics



class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        print(serializer.data)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug):
        try:
            # Query the product by category_slug and product_slug
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def search_products(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)  
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    return Response([], status=200)  

