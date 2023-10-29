from rest_framework import serializers

from habit.models import Habit
from overall.validators import HabitValidation, HabitPeriodicityValidation, HabitCreateValidation


class HabitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[HabitValidation()])
    periodicity_in_week = serializers.IntegerField(validators=[HabitPeriodicityValidation()])
    owner = serializers.SerializerMethodField()

    def get_owner(self, instance):
        instance.owner = self.context['request'].user
        instance.save()
        return instance.owner.id

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitCreateValidation()]
