import factory
from faker import Faker
from .models import User

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.user_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    password = factory.PostGenerationMethodCall('set_password', 'password123')
    # password_confirmation = factory.PostGenerationMethodCall('set_password', 'password123')


