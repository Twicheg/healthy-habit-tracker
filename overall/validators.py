import datetime

from rest_framework import serializers

from habit.models import Habit


class HabitValidation:
    def __call__(self, value):
        if value > 120:
            raise serializers.ValidationError('Время на выполнение не должно превышать 120 секунд')


class HabitTimeValidation:
    def __call__(self, value):
        if (value.replace(tzinfo=None)-datetime.datetime.now().replace(microsecond=False)).days > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

