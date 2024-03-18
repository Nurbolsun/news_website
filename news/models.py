from django.db import models
from account.models import User


class Tag(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class NewsCategory(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"


class News(models.Model):
    news_category = models.ForeignKey(
        NewsCategory, null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория новости'
    )
    tag = models.ManyToManyField(
        Tag, verbose_name='Тег'
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=150
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to="images/news",
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    count_views = models.IntegerField(default=0)
    count_likes = models.IntegerField(default=0)
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=True
    )
    user = models.ForeignKey(
        User, verbose_name="Пользователь",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Slider(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(
        upload_to="images/slider",
        null=True, blank=True
    )
    title = models.TextField()
    subtitle = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"