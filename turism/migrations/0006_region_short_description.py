# Generated by Django 4.2.7 on 2024-01-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turism', '0005_alter_placeimage_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='short_description',
            field=models.CharField(default=1, max_length=255, verbose_name='Краткое описание'),
            preserve_default=False,
        ),
    ]