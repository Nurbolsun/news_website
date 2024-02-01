from django.db import models
from news.models import Category


# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Роль для пользователя"
        verbose_name_plural = "Роль для пользователя"


class User(models.Model):
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField("Электронная почта", unique=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField("Верифицирован", default=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользовател"
        verbose_name_plural = "Пользователи"
