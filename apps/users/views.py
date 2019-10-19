from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Token, User
from .serializers import LoginSerializer, UserProfileSerializer, UserSerializer


class RegisterView(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = User.objects.create(email=email)
            user.set_password(password)
            user.groups.add(Group.objects.get(name="user"))
            user.save()
            serializer = UserProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        print(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
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
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if not user:
                return Response(
                    {"detail": "Invalid Credentials or activate account"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token = Token.objects.create(user=user)

            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def get(self, request, format=None):
        Token.objects.get(key=request.auth).delete()
        return Response(status=status.HTTP_200_OK)
