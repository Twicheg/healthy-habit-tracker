from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="test@test.com", password='12345')
        self.user.is_active = True
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.set_password(self.user.password)
        self.client.force_authenticate(user=self.user)

    def test_getting_user_list(self):
        url = reverse('users:users_list')
        response = self.client.get(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_user(self):
        url = reverse('users:user_create')
        data = {
            "email": "test10@test.com",
            "password": "12345",
            "tg_username": "test"
        }
        response = self.client.post(
            url,
            data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_destroy_user(self):
        url = reverse('users:user_destroy', args=[self.user.pk])
        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.user.is_staff = False
        self.user.is_superuser = False

        response = self.client.delete(
            url
        )
        self.assertEquals(
            response.json(),
            {'detail': 'You do not have permission to perform this action.'}
        )
