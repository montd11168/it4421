import random
import string
from datetime import datetime
from uuid import uuid4
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.management.commands import loaddata
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Token
from .serializers import (
    LoginSerializer,
    PasswordResetSerializer,
    UserProfileSerializer,
    UserProfileUpdateSerializer,
    UserRegisterSerializer,
    UserSerializer,
    VerificationSerializer,
)

User = get_user_model()


def password_reset(length=8):
    random_string = string.ascii_letters + string.digits
    return "".join(random.choice(random_string) for i in range(length))


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class RegisterView(APIView):
    def get(self, request, format=None):
        serializer = VerificationSerializer(data=request.query_params)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            verificate_code = serializer.validated_data["verificate_code"]
            if User.objects.filter(email=email, verificate_code=verificate_code).exists():
                User.objects.filter(email=email).update(is_active=True)
                return Response(
                    {"message": "Your account has been activated."}, status=status.HTTP_200_OK
                )
            return Response(
                {"message": "Email or verificate code is incorrect."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            if not User.objects.filter(email=email).exists():
                password = serializer.validated_data["password"]
                # group = Group.objects.get(name="user")
                try:
                    group = Group.objects.get(name="user")
                except Group.DoesNotExist:
                    return Response(
                        {
                            "message from Văn": "Biết ngay là sẽ gặp lỗi này mà. "
                            + "Vô http://127.0.0.1:8000/admin/auth/group/add/ thêm group: user đã các bạn nhé!"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                user = User.objects.create(**serializer.data)
                user.set_password(password)
                user.groups.add(group)
                user.is_active = False
                user.verificate_code = uuid4()
                user.save()
                auth_url = (
                    settings.BACKEND_HOST
                    + "/users/register?email={}&verificate_code={}".format(
                        email, user.verificate_code
                    )
                )
                send_mail(
                    "IT4421 Confirm.",
                    auth_url,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return Response(
                    {"message": "Please check your email to confirm."},
                    status=status.HTTP_201_CREATED,
                )
            return Response({"message": "Email Exists."}, status=status.HTTP_400_BAD_REQUEST)
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
            user.last_login = datetime.now()
            user.save()
            token = Token.objects.create(user=user)
            response = {
                "token": token.key,
                "is_activate": user.is_active,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
            }
            return Response(response, status=status.HTTP_200_OK)
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
