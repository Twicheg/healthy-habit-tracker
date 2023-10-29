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
