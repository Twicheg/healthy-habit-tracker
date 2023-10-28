from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "place", "time", "action", "sign_of_a_pleasant_habit", "related_habit_id",
                    "periodicity_in_week", "reward", "time_to_complete", "is_public", ]
