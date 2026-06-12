from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class SignupViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('signup')

    def test_signup_success(self):
        payload = {
            "email":"azad+testmail@gmail.com",
            "password":"userpassword",
            "confirm_password":"userpassword"
        }
        response = self.client.post(self.url,payload,format="json")
        print(response.data,"res data")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(
            User.objects.count(),
            1
        )