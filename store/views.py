from tkinter.tix import Tree
from typing import Collection

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import CollectionSerializers, ProductSerializers


# Create your views here.
@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializers(
        queryset, many=Tree, context={'request': request})
    return Response(serializer.data)


@api_view()
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializers(product, context={'request': request})
    return Response(serializer.data)

    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializers(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)


@api_view()
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk)
    serializer = CollectionSerializers(
        collection, context={'request': request})
    return Response(serializer.data)
