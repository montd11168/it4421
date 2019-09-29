from rest_framework import serializers

from .models import Comment, Product, Supplier, Vote


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

    class Meta:
        model = Product
        fields = [
            "id",
            "supplier",
            "name",
            "price",
            "descript",
            "count",
            "image",
            "votes",
            "comments",
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "image"]
