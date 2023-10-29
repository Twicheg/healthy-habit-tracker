from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from habit.models import Habit
from users.models import User


# coverage run --source='.' --omit='*/migrations/*','*/management/*','*/__init__.py' manage.py test && coverage report

class LessonTestCase(APITestCase):
    def setUp(self):
        data = {
            "place": "place1",
            "time": "10:10:10",
            "action": "testaction",
            # "related_habit": 3,
            "sign_of_a_pleasant_habit": True,
            "periodicity_in_week": 3,
            "reward": "candy",
            "time_to_complete": 100,
            "is_public": True
        }

        self.habit = Habit.objects.create(**data)

        self.client = APIClient()
        self.user = User.objects.create(email="test@test.com", password='12345')
        self.user.is_active = True
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.set_password(self.user.password)
        self.client.force_authenticate(user=self.user)

    def test_getting_habit_list(self):
        url = reverse('habit:habit_list')
        response = self.client.get(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
