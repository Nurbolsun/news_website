from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models

from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    ADMIN = 'ADMIN'
    SUPER_ADMIN = 'SUPER_ADMIN'
    EDITOR = 'EDITOR'
    JOURNALIST = 'JOURNALIST'
    GUEST = 'GUEST'
    ROLES = (
            (ADMIN, 'ADMIN'),
            (SUPER_ADMIN, 'SUPER_ADMIN'),
            (EDITOR, 'EDITOR'),
            (JOURNALIST, 'JOURNALIST'),
            (GUEST, 'GUEST'),
    )

    MALE = 'МУЖСКОЙ'
    FEMALE = "ЖЕНСКИЙ"
    GENDER = (
        (MALE, 'МУЖСКОЙ'),
        (FEMALE, "ЖЕНСКИЙ"),
    )
    username = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Электронная почта')
    role = models.CharField(max_length=255, choices=ROLES, default=GUEST, verbose_name='Роль')
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    gender = models.CharField(max_length=20, choices=GENDER, null=True, blank=True, verbose_name='Пол')
    birthdate = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
