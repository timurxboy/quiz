from rest_framework import generics, status
from rest_framework.response import Response

from ..serializers.authorization import UserSerializer

from django.contrib.auth.models import User
from rest_framework import permissions

from django.contrib.auth.hashers import make_password


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        email = serializer.validated_data.get('email')
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return Response(
            data={
                "username": username,
                "email": email,
                "first_name": first_name,
                "last_name": last_name
            },
            status=status.HTTP_201_CREATED
        )
