from rest_framework import serializers

from habit.models import Habit


class HabitValidation:
    def __call__(self, value):
        if value > 120:
            raise serializers.ValidationError('Время на выполнение не должно превышать 120 секунд')


class HabitPeriodicityValidation:
    def __call__(self, value):
        if value < 1:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


class HabitCreateValidation:
    def __call__(self, value):
        if not value.get('related_habit') and not value.get('sign_of_a_pleasant_habit'):
            raise serializers.ValidationError('привычка должна быть приятной или ссылаться на приятную')

        if value.get('related_habit') and value.get('sign_of_a_pleasant_habit'):
            raise serializers.ValidationError('привычка может быть либо приятной либо связанной')

        if value.get('related_habit') and value.get('reward'):
            raise serializers.ValidationError('нельзя указывать награду за связанную привычку')

        if value.get('related_habit') and not Habit.objects.get(
                id=value.get('related_habit').id).sign_of_a_pleasant_habit:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.')
