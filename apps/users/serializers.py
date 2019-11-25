from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(serializers.Serializer):
    last_login = serializers.DateTimeField(required=False)
    date_joined = serializers.DateTimeField(required=False)
    email = serializers.ReadOnlyField()
    username = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    address = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)


class UserProfileUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    address = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    address = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verificate_code = serializers.UUIDField()


class PermissionSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
