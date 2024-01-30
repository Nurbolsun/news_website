from django.db import models
from solo.models import SingletonModel
from multiselectfield import MultiSelectField


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


class Region(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото'
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('name',)


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
        verbose_name='Фото'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
    )
    MONTH_CHOICES = (
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь')
    )

    month = MultiSelectField(
        choices=MONTH_CHOICES, max_choices=12,
        max_length=255, verbose_name='Месяц',
        blank=True, null=True
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

