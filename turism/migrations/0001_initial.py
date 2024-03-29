# Generated by Django 5.0.1 on 2024-03-18 09:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('img', models.ImageField(upload_to='images/turism/', verbose_name='Фото')),
                ('caption', models.CharField(max_length=100, verbose_name='Надпись')),
                ('page', models.TextField(blank=True, null=True, verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Фото')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('link', models.CharField(max_length=150, verbose_name='Cсылка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Месяц',
                'verbose_name_plural': 'Месяцы',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/turism/', verbose_name='Фото')),
                ('short_description', models.CharField(max_length=255, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('img_1', models.ImageField(upload_to='images/turism/', verbose_name='Фото 1')),
                ('img_2', models.ImageField(upload_to='images/turism/', verbose_name='Фото 2')),
                ('img_3', models.ImageField(upload_to='images/turism/', verbose_name='Фото 3')),
                ('description_1', models.TextField(verbose_name='Описание 1')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Изображение')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Изображение 2')),
                ('title', models.CharField(blank=True, max_length=25, null=True, verbose_name='Заголовок')),
                ('description_1', models.TextField(blank=True, null=True, verbose_name='Описание 1')),
                ('description_2', models.TextField(blank=True, null=True, verbose_name='Описание 2')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Изображение 3')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Изображение 4')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='images/turism/', verbose_name='Изображение 5')),
            ],
            options={
                'verbose_name': 'Путешествие',
                'verbose_name_plural': 'Путешествия',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('video_url', models.FileField(upload_to='videos/turism/', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Видео для заставки',
                'verbose_name_plural': 'Видео для заставки',
            },
        ),
        migrations.CreateModel(
            name='ConsultationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(blank=True, max_length=255, null=True, verbose_name='Куда бы вы хотели поехать?')),
                ('travel_month', models.CharField(blank=True, max_length=20, null=True, verbose_name='Когда вы хотели бы поехать? (Месяц)')),
                ('travel_year', models.IntegerField(blank=True, null=True, verbose_name='Когда вы хотели бы поехать? (Год)')),
                ('duration', models.CharField(blank=True, max_length=50, null=True, verbose_name='Надолго ли?')),
                ('num_travelers', models.IntegerField(blank=True, null=True, verbose_name='Сколько человек путешествует?')),
                ('budget_per_person', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Сколько вы хотели бы потратить на одного человека?')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Еще какие-нибудь комментарии или пожелания?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка на консультацию',
                'verbose_name_plural': 'Заявки на консультацию',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/turism/', verbose_name='Фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('categories', models.ManyToManyField(related_name='places', to='turism.category', verbose_name='Категории')),
                ('months', models.ManyToManyField(blank=True, related_name='places', to='turism.month', verbose_name='Месяц')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='turism.region', verbose_name='Регион')),
                ('traveller', models.ManyToManyField(blank=True, related_name='places', to='turism.traveller', verbose_name='Путешествие')),
            ],
            options={
                'verbose_name': 'Место отдыха',
                'verbose_name_plural': 'Места отдыха',
                'ordering': ('name', 'region'),
            },
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/turism/', verbose_name='Фото')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_images', to='turism.place', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Изображение места',
                'verbose_name_plural': 'Изображения места',
            },
        ),
    ]
