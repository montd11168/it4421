from drf_roles.mixins import RoleViewSetMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Comment, Item, Order, Product, ProductColor, ProductImage, Supplier, Vote
from .serializers import (
    CommentSerializer,
    ItemSerializer,
    OrderSerializer,
    ProductColorSerializer,
    ProductImageSerializer,
    ProductSerializer,
    SupplierSerializer,
    VoteSerializer,
)


class SupplierViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SProductViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(supplier=self.kwargs["supplier_pk"])


class ProductViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ItemViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data["product"]
            quantity = serializer.validated_data["quantity"]
            item = Item.objects.filter(product=product)
            if not item:
                Item.objects.create(product=product, quantity=quantity, user=request.user)
            else:
                item[0].quantity += quantity
                item[0].save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CommentViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(product=self.kwargs["product_pk"])


class VoteViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = VoteSerializer

    def get_queryset(self):
        return Vote.objects.filter(product=self.kwargs["product_pk"])


class ImageViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product=self.kwargs["product_pk"])


class ColorViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductColorSerializer

    def get_queryset(self):
        return ProductColor.objects.filter(product=self.kwargs["product_pk"])
