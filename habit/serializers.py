from rest_framework import serializers

from habit.models import Habit
from overall.validators import HabitValidation, HabitTimeValidation


class HabitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[HabitValidation()])
    time = serializers.DateTimeField(validators=[HabitTimeValidation()])
    user = serializers.SerializerMethodField()

    def get_user(self, instance):
        return self.context['request'].user.email

    def create(self, validated_data):
        if validated_data.get('related_habit') and validated_data.get('reward'):
            raise serializers.ValidationError('нельзя указывать награду за связанную привычку')
        if validated_data.get('related_habit').id not in [i.id for i in Habit.objects.filter(sign_of_a_pleasant_habit=True)]:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        obj = Habit.objects.create(**validated_data)
        return obj

    class Meta:
        model = Habit
        fields = '__all__'
