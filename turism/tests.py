from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker

from account.factories import UserFactory
from turism.models import Feedback
from turism.factories import FeedbackFactory


fake = Faker()

class FeedbackAPITest(APITestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.feedbacks = FeedbackFactory.create_batch(50, user=self.user)
    def test_create_feedback(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('feedback-list-create')
        comment = fake.text()
        response = self.client.post(url, {'comment': comment})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Feedback.objects.filter(user=self.user, comment=comment).exists())

    def test_feedback(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('feedback-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 50)

