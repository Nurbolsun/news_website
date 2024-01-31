from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def creat_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser mast have is_superuser=True")
        return self.creat_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField("Электронная почта", unique=True)
    # password = models.CharField(max_length=128)
    is_verified = models.BooleanField("Верифицирован", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

