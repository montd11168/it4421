from drf_roles.mixins import RoleViewSetMixin
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.shortcuts import render
from .models import Comment, Cart, Order, Product, ProductImage, Supplier, Vote
from .serializers import (
    CommentSerializer,
    CartSerializer,
    CartCreateSerializer,
    CartUpdateSerializer,
    OrderSerializer,
    OrderCreateSerializer,
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


class CartViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def create(self, request):
        serializer = CartCreateSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data["product_id"]
            quantity = serializer.validated_data["quantity"]
            cart, created = Cart.objects.get_or_create(product_id=product_id, user=request.user)
            if created:
                cart.quantity = quantity
            else:
                cart.quantity += quantity
            cart.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = CartUpdateSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data["quantity"]
            Cart.objects.filter(pk=pk).update(quantity=quantity)
            cart = Cart.objects.get(pk=pk)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     cart = Cart.objects.filter(user=self.request.user, pk=pk)
    #     print(cart)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            cart_id = serializer.validated_data["cart_id"]
            order = Order.objects.create(user=request.user)
            cart = Cart.objects.filter(pk=cart_id).update(order=order)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# add order with list cart