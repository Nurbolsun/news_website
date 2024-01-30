# Generated by Django 5.0.1 on 2024-01-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_news_count_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('title', models.TextField()),
                ('subtitle', models.TextField()),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
            },
        ),
    ]