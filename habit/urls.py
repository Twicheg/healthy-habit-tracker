from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitApiList, HabitApiCreate, HabitApiUpdate, HabitApiDestroy, HabitApiRetrieve

app_name = HabitConfig.name

urlpatterns = [
    path('habit/', HabitApiList.as_view(), name='habit_list'),
    path('habit/create/', HabitApiCreate.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitApiUpdate.as_view(), name='habit_update'),
    path('habit/<int:pk>/', HabitApiRetrieve.as_view(), name='habit_retrieve'),
    path('habit/delete/<int:pk>/', HabitApiDestroy.as_view(), name='habit_destroy'),
]
