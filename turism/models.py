from django.db import models
from solo.models import SingletonModel


class HomePage(SingletonModel):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Video(SingletonModel):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    video_url = models.FileField(
        upload_to='videos/turism/',
        verbose_name='Видео'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео для заставки'
        verbose_name_plural = 'Видео для заставки'


class Region(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото'
    )
    short_description = models.CharField(
        max_length=255,
        verbose_name='Краткое описание'
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('id',)


class Category(models.Model):
    image = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Month(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=25, unique=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images/turism/',
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Месяц'
        verbose_name_plural = 'Месяцы'


class Traveller(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=25, unique=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images/turism/',
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Путешествие'
        verbose_name_plural = 'Путешествия'


class Place(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    address = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name='Адрес'
    )
    phone_number = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name='Телефон'
    )
    image = models.ImageField(
        upload_to='images/turism/',
        blank=True, null=True, default='',
        verbose_name='Фото'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
    )
    months = models.ManyToManyField(
        Month, related_name='places',
        verbose_name='Месяц', blank=True
    )
    traveller = models.ManyToManyField(
        Traveller, related_name='places',
        verbose_name='Путешествие', blank=True
    )
    categories = models.ManyToManyField(
        Category, related_name='places',
        verbose_name='Категории'
    )
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE,
        related_name='places',
        verbose_name='Регион'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место отдыха'
        verbose_name_plural = 'Места отдыха'
        ordering = ('name', 'region')


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE,
        related_name='place_images', verbose_name='Место'
    )
    image = models.ImageField(
        upload_to='images/turism/',
        blank=True, null=True, default='',
        verbose_name='Фото'
    )
    def __str__(self):
        return f'Фото для {self.place.name}'


    class Meta:
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения места'
