from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . serializers import ProductSerializer
from . models import Product

# Create your views here.
"""
@api_view(['GET'])
def apiOverview(request):
     api_urls = {
         'List': '/product-list/',
         'Detail_view': '/product-detail/<int:id>',
         'Create': '/product-create',
         'Update': '/product-update/<int:id>',
         'Delete': '/product-detail/<int:id>'
     }
     return Response(api_urls);
"""
@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewProduct(request, pk): #pk - primary key
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response("Items deleted successfully!")