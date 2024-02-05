from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError("Электронная почта должна быть обязательным")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('Пароль не должен быть пустым')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save()
        return user


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
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

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
