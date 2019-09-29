from django.shortcuts import render
from rest_framework import viewsets

from .models import Supplier, Product
from .serializers import SupplierSerializer, ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(supplier=self.kwargs['supplier_pk'])