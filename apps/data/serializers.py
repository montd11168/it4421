from rest_framework import serializers

from .models import Comment, Export, Import, Product, ProductColor, ProductImage, Supplier, Vote


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "descript"]


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ["color", "price", "count"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = ["user", "content"]


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Vote
        fields = ["user", "value"]


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.ReadOnlyField(source="supplier.name")
    votes = VoteSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "supplier",
            "name",
            "descript",
            "operating_system",
            "ram",
            "rom",
            "battery",
            "front_camera",
            "rear_camera",
            "sim",
            "screen",
            "memory_card",
            "votes",
            "comments",
            "colors",
            "images",
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "logo"]
