from rest_framework import serializers

from .models import (
    Comment,
    Export,
    Import,
    Cart,
    Order,
    Product,
    ProductImage,
    Supplier,
    Vote,
)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(serializers.Serializer):
    content = serializers.CharField()


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Vote
        fields = "__all__"


class VoteCreateSerializer(serializers.Serializer):
    value = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.ReadOnlyField(source="supplier.name")
    images = ProductImageSerializer(many=True, read_only=True)
    votes = VoteSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ("user",)


class CartCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CartUpdateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    carts = CartSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField()
    