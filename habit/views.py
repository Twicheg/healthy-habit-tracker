from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.serializers import HabitListSerializer, HabitCreateSerializer
from overall.paginations import MyPagination
from overall.permissions import OwnerPermission


class HabitApiList(generics.ListAPIView):
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(owner=self.request.user)
        return queryset


class PublicHabitApiList(generics.ListAPIView):
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitApiCreate(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]


class HabitApiUpdate(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated & OwnerPermission]


class HabitApiRetrieve(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated & OwnerPermission]


class HabitApiDestroy(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated & OwnerPermission]
