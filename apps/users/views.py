from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Token, User
from .serializers import (
    LoginSerializer,
    UserProfileSerializer,
    UserSerializer,
    UserRegisterSerializer,
    UserProfileUpdateSerializer,
    PasswordResetSerializer,
)
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated


def password_reset(length=8):
    random_string = string.ascii_letters + string.digits
    return "".join(random.choice(random_string) for i in range(length))


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = User.objects.create(email=email)
            user.set_password(password)
            user.groups.add(Group.objects.get(name="user"))
            user.save()
            User.objects.filter(pk=user.id).update(**serializer.validated_data)
            user = User.objects.get(pk=user.id)
            # serializer = UserSerializer(user)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        serializer = UserProfileUpdateSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.filter(email=request.user).update(**serializer.data)
            user = User.objects.get(email=request.user)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            if not user:
                return Response(
                    {"detail": "Invalid Credentials or activate account"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token = Token.objects.create(user=user)

            return Response({"Token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request, format=None):
        Token.objects.get(key=request.auth).delete()
        return Response(status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    def post(self, request, format=None):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            new_password = password_reset()
            user.set_password(new_password)
            user.save()
            send_mail(
                "IT4421 Password Reset",
                new_password,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            Token.objects.filter(user=user).delete()
            return Response({"message": "Please check your email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
