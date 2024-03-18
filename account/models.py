from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
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


class User(AbstractUser):
    username = models.CharField(
        max_length=25, unique=False,
        verbose_name='Имя пользователя',
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=60, unique=True,
        default='Еще не заполнен'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, blank=True,
        verbose_name='Фото пользователя'
    )
    phone_number = models.CharField(
        max_length=16, verbose_name='Номер телефона',
        unique=True, blank=True, null=True
    )
    ROLE = (
            ('ADMIN', 'Админ'),
            ('JOURNALIST', 'Журналист'),
    )
    GENDER = (
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
        ('OTHER', 'Другое')
    )
    role = models.CharField(
        max_length=200, choices=ROLE,
        verbose_name='Роль',
        blank=True, null=True
    )
    gender = models.CharField(
        max_length=20, choices=GENDER,
        null=True, blank=True,
        verbose_name='Пол'
    )
    age = models.IntegerField(
        verbose_name='Возраст',
        blank=True, null=True
    )
    otp_reset = models.CharField(max_length=6, blank=True, null=True)
    otp_reset_created_at = models.DateTimeField(blank=True, null=True)
    otp_verified = models.BooleanField(default=False)

    def otp_expired(self):
        if self.otp_reset_created_at:
            expiration_time = self.otp_reset_created_at + timedelta(minutes=5)
            return timezone.now() > expiration_time
        return True

    def save(self, *args, **kwargs):
        if self.otp_reset and not self.otp_reset_created_at:
            self.otp_reset_created_at = timezone.now()
        elif self.otp_reset and self.otp_reset_created_at:
            self.otp_reset_created_at = timezone.now()

        super().save(*args, **kwargs)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'email:{self.email}, имя пользователя: {self.username}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя'
    )
    subscribed = models.BooleanField(default=True)
    unsubscribed = models.BooleanField(default=False)
    newsletters = models.ManyToManyField(
        'Newsletter', blank=True,
        verbose_name='Полученные рассылки'
    )

    def __str__(self):
        return f"{self.username} ({self.email})"
    class Meta:
        verbose_name='Подписанные на рассылку'
        verbose_name_plural='Подписанные на рассылку'


class Newsletter(models.Model):
    subject = models.CharField(
        max_length=255,
        verbose_name='Тема рассылки'
    )
    content = models.TextField(
        verbose_name='Содержание рассылки'
    )
    sent_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Отправлено'
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
