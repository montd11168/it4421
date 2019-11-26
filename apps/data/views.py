from drf_roles.mixins import RoleViewSetMixin
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.shortcuts import render
from .models import Comment, Cart, Order, Product, ProductImage, Supplier, Vote
from .serializers import (
    CommentSerializer,
    CommentCreateSerializer,
    CartSerializer,
    CartCreateSerializer,
    CartUpdateSerializer,
    OrderSerializer,
    OrderCreateSerializer,
    ProductImageSerializer,
    ProductSerializer,
    ProductCreateSerializer,
    SupplierSerializer,
    VoteSerializer,
    VoteCreateSerializer,
)
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
import json


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

    def create(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            supplier_id = serializer.validated_data["supplier_id"]
            name = serializer.validated_data["name"]
            product, created = Product.objects.get_or_create(supplier_id=supplier_id, name=name)
            if created:
                Product.objects.filter(pk=product.id).update(**serializer.validated_data)
                return Response(status=status.HTTP_200_OK)
            return Response({"message": "Product Exists."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user, order=None)
        for cart in queryset:
            product = Product.objects.get(pk=cart.product.id)
            cart.detail_products = product
        return queryset

    def create(self, request):
        serializer = CartCreateSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data["product_id"]
            quantity = serializer.validated_data["quantity"]
            cart, created = Cart.objects.get_or_create(
                product_id=product_id, user=request.user, order=None
            )
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
            product = Product.objects.get(pk=cart.product.id)
            cart.detail_products = product
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request):
        serializer = OrderCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            order = Order.objects.create(user=request.user)
            for cart in serializer.validated_data:
                cart_id = cart["cart_id"]
                cart = Cart.objects.filter(pk=cart_id).update(order=order)
                cart = Cart.objects.get(pk=cart_id)
                order.total += cart.quantity * cart.product.listed_price
                order.save()
            serializer = OrderSerializer(order)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Order.objects.filter(pk=pk).update(status="ĐÃ HỦY")
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(product=self.kwargs["product_pk"])

    def create(self, request, product_pk=None):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data["content"]
            product = Product.objects.get(pk=product_pk)
            comment = Comment.objects.create(product=product, content=content, user=request.user)
            serializer = CommentSerializer(comment)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = VoteSerializer

    def get_queryset(self):
        return Vote.objects.filter(product=self.kwargs["product_pk"])

    def create(self, request, product_pk=None):
        serializer = VoteCreateSerializer(data=request.data)
        if serializer.is_valid():
            value = serializer.validated_data["value"]
            product = Product.objects.get(pk=product_pk)
            vote = Vote.objects.create(product=product, value=value, user=request.user)
            product.voting = Vote.objects.filter(product=product).aggregate(Avg("value"))[
                "value__avg"
            ]
            product.save()
            serializer = VoteSerializer(vote)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product=self.kwargs["product_pk"])
