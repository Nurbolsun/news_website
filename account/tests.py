from django.core import mail
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.test import override_settings
from django.shortcuts import get_object_or_404

from .models import User
from .factories import UserFactory


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class RegistrationAPITest(APITestCase):
    def test_registration(self):
        url = reverse('register')
        user_data = UserFactory.build()

        response = self.client.post(url, {
            'username': user_data.username,
            'email': user_data.email,
            'password': 'password123',
            'password_confirmation': 'password123',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], f'Регистрация успешна, {user_data.username}. Проверьте электронную почту для подтверждения.')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'LifeKG')
        self.assertEqual(mail.outbox[0].to, [user_data.email])


    def test_register_with_invalid_conf_password(self):
        url = reverse('register')
        user_data = UserFactory.build()
        response = self.client.post(url, {
            'username': user_data.username,
            'email': user_data.email,
            'password': 'password123',
            'password_confirmation': 'invalid'
        })
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message')


    def test_register_exist_email(self):
        User.objects.create(email='user@gmail.com')
        url = reverse('register')
        user_data = UserFactory.build(email='user@gmail.com')
        response = self.client.post(url, {
            'username': user_data.username,
            'email': user_data.email,
            'password': 'password123',
            'password_confirmation': 'password123',
        })
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)


class LoginAPITest(APITestCase):
    def test_login_with_valid_credentials(self):
        user = UserFactory.create()
        url = reverse('login')
        data = {
            'email': user.email,
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' in response.data)
        self.assertTrue('access' in response.data)

    def test_login_with_invalid_email(self):
        url = reverse('login')
        data = {
            'email': 'invalid_email@gmail.com',
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('message', response.data)

    def test_login_with_invalid_password(self):
        user = User.objects.create(email='test@example.com', password='testpassword')
        url = reverse('login')
        data = {
            'email': user.email,
            'password': 'invalid_password'
        }
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

