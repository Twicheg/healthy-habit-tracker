from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        data = {
            "place": "place1",
            "time": "10:10:10",
            "action": "testaction",
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
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('habit:habit_create')
        data = {
            "place": "place1",
            "time": "10:10:10",
            "action": "testaction",
            "sign_of_a_pleasant_habit": True,
            "periodicity_in_week": 3,
            "reward": "candy",
            "time_to_complete": 100,
            "is_public": True
        }
        response = self.client.post(
            url,
            data
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_validator_time(self):
        url = reverse('habit:habit_create')
        data = {
            "place": "place1",
            "time": "10:10:10",
            "action": "testaction",
            "sign_of_a_pleasant_habit": True,
            "periodicity_in_week": 3,
            "reward": "candy",
            "time_to_complete": 130,
            "is_public": True
        }
        response = self.client.post(
            url,
            data
        )
        self.assertEquals(response.json(), {'time_to_complete': ['Время на выполнение не должно превышать 120 секунд']})

    def test_validator_related_habit(self):
        url = reverse('habit:habit_create')
        data = {
            "place": "place1",
            "time": "10:10:10",
            "action": "testaction",
            "sign_of_a_pleasant_habit": True,
            "periodicity_in_week": 3,
            "related_habit": self.habit.id,
            "reward": "candy",
            "time_to_complete": 100,
            "is_public": True
        }
        response = self.client.post(
            url,
            data
        )
        self.assertEquals(response.json(), {'non_field_errors': ['привычка может быть либо приятной либо связанной']})

    def test_getting_habit_list(self):
        url = reverse('habit:habit_list')
        response = self.client.get(
            url
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_getting_habit_retrieve(self):
        url = reverse('habit:habit_retrieve', args=[self.habit.id])
        response = self.client.get(
            url,
        )
        self.assertEquals = (response.json()["action"], "testaction")

    def test_getting_habit_patch(self):
        url = reverse('habit:habit_update', args=[self.habit.id])
        data = {
            "action": "newaction"
        }
        response = self.client.patch(
            url,
            data
        )
        self.assertEquals(response.json()['action'], "newaction")

    def test_public_list(self):
        url = reverse('habit:habit_public_list')
        response = self.client.get(
            url
        )

        self.assertEquals(None not in [i["is_public"] for i in response.json()], True)

    def test_getting_habit_delete(self):
        url = reverse('habit:habit_destroy', args=[self.habit.id])
        data = {
            "action": "newaction"
        }
        response = self.client.delete(
            url,
            data
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
