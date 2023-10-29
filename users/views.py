from rest_framework import generics, permissions

from users.models import User
from users.serializers import UserSerializer


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new = serializer.save()
        new.set_password(new.password)
        new.save()


class UserDestroyApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
