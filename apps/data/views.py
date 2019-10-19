from rest_framework import viewsets

from .models import Comment, Item, Order, Product, Supplier, Vote, ProductColor, ProductImage
from .serializers import (
    CommentSerializer,
    ItemSerializer,
    OrderSerializer,
    ProductSerializer,
    SupplierSerializer,
    VoteSerializer,
    ProductColorSerializer,
    ProductImageSerializer,
)


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(supplier=self.kwargs["supplier_pk"])


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(product=self.kwargs["product_pk"])


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer

    def get_queryset(self):
        return Vote.objects.filter(product=self.kwargs["product_pk"])


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product=self.kwargs["product_pk"])


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ProductColorSerializer

    def get_queryset(self):
        return ProductColor.objects.filter(product=self.kwargs["product_pk"])
