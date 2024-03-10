from django.db import models
from django.conf import settings
from solo.models import SingletonModel
from account.models import User


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
    img_1 = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото 1'
    )
    img_2 = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото 2'
    )
    img_3 = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото 3'
    )
    description_1 = models.TextField(
        verbose_name='Описание 1',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('id',)


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Текст',
        blank=True, null=True
    )
    img = models.ImageField(
        upload_to='images/turism/',
        verbose_name='Фото'
    )
    caption = models.CharField(
        max_length=100,
        verbose_name='Надпись'
    )
    page = models.TextField(
        verbose_name='Страница',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


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
    img_2 = models.ImageField(
        verbose_name='Изображение 2',
        upload_to='images/turism/',
        blank=True, null=True
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=25, blank=True, null=True,
    )
    description_1 = models.TextField(
        verbose_name='Описание 1',
        blank=True, null=True
    )
    description_2 = models.TextField(
        verbose_name='Описание 2',
        blank=True, null=True
    )
    img_3 = models.ImageField(
        verbose_name='Изображение 3',
        upload_to='images/turism/',
        blank=True, null=True
    )
    img_4 = models.ImageField(
        verbose_name='Изображение 4',
        upload_to='images/turism/',
        blank=True, null=True
    )
    img_5 = models.ImageField(
        verbose_name='Изображение 5',
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


class Feedback(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Пользователь'
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.created_at}"

    class Meta:
        verbose_name='Обратная связь'
        verbose_name_plural='Обратная связь'


class Commentary(models.Model):
    image = models.ImageField(
        upload_to='images/turism/',
        blank=True, null=True,
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
    )
    link = models.CharField(
        max_length=150,
        verbose_name='Cсылка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class ConsultationRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name = 'Пользователь'
    )
    destination = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Куда бы вы хотели поехать?'
    )
    travel_month = models.CharField(
        max_length=20,
        blank=True, null=True,
        verbose_name='Когда вы хотели бы поехать? (Месяц)'
    )
    travel_year = models.IntegerField(
        blank=True, null=True,
        verbose_name='Когда вы хотели бы поехать? (Год)'
    )
    duration = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name= 'Надолго ли?'
    )
    num_travelers = models.IntegerField(
        blank=True, null=True,
        verbose_name='Сколько человек путешествует?'
    )
    budget_per_person = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True,
        verbose_name='Сколько вы хотели бы потратить на одного человека?'
    )
    comments = models.TextField(
        blank=True, null=True,
        verbose_name='Еще какие-нибудь комментарии или пожелания?'
    )

    def __str__(self):
        return f"Заявка на консультацию в {self.destination} от {self.user.username}"

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'
