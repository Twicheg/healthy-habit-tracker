from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from habit.models import Habit
from habit.serializers import HabitListSerializer, HabitCreateSerializer


class HabitApiList(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer


class HabitApiCreate(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]


class HabitApiUpdate(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer


class HabitApiRetrieve(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer


class HabitApiDestroy(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
