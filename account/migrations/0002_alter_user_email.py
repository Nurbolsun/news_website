# Generated by Django 5.0.1 on 2024-02-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='Еще не заполнен', max_length=60, unique=True, verbose_name='Почта'),
        ),
    ]