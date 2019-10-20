from rest_framework import serializers
from .models import User


class UserProfileSerializer(serializers.Serializer):
    last_login = serializers.DateTimeField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    date_joined = serializers.DateTimeField(required=False)
    email = serializers.ReadOnlyField(required=False)
    username = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    address = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)
    avatar = serializers.ImageField(required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
