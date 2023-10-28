from rest_framework import serializers

from habit.models import Habit
from overall.validators import HabitValidation, HabitPeriodicityValidation


class HabitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[HabitValidation()])
    periodicity_in_week = serializers.IntegerField(validators=[HabitPeriodicityValidation()])

    class Meta:
        model = Habit
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.get('related_habit') and validated_data.get('sign_of_a_pleasant_habit'):
            raise serializers.ValidationError('привычка может быть либо приятной либо связанной')

        if validated_data.get('related_habit') and validated_data.get('reward'):
            raise serializers.ValidationError('нельзя указывать награду за связанную привычку')

        if validated_data.get('related_habit') and not Habit.objects.get(
                id=validated_data.get('related_habit').id).sign_of_a_pleasant_habit:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        validated_data["owner"] = self.context['request'].user

        obj = Habit.objects.create(**validated_data)
        return obj
