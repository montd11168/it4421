from rest_framework import serializers

from .models import (
    Comment,
    Export,
    Import,
    Item,
    Order,
    Product,
    # ProductColor,
    ProductImage,
    Supplier,
    Vote,
)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


# class ProductColorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductColor
#         fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Comment
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Vote
        fields = "__all__"


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


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ("user",)


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
