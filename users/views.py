from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDestroyApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
