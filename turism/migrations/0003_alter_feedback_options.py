# Generated by Django 5.0.1 on 2024-02-15 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turism', '0002_alter_commentary_image_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
    ]
