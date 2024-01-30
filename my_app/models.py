from django.db import models
from user_app.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class News(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    title = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField("Описание")
    photo = models.ImageField(upload_to="photo_for_news", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    count_views = models.IntegerField(default=0)
    is_active = models.BooleanField(verbose_name="Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Slider(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="photo_for_slider", null=True, blank=True)
    title = models.TextField()
    subtitle = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдер"