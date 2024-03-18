from factory import Faker as FactoryFaker
from factory.django import DjangoModelFactory

from account.models import User
from .models import Feedback


class FeedbackFactory(DjangoModelFactory):
    class Meta:
        model = Feedback

    user = FactoryFaker('user')
    comment = FactoryFaker('text')
