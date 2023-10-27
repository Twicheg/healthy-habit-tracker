from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ["user", "place", "time", "action", "sign_of_a_pleasant_habit", "related_habit",
                    "periodicity", "reward", "time_to_complete", "sign_of_publicity", "related_habit_fk"]
