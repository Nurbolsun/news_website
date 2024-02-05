# Generated by Django 4.2.7 on 2024-02-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turism', '0014_alter_place_months_alter_place_traveller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='months',
            field=models.ManyToManyField(blank=True, related_name='places', to='turism.month', verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='place',
            name='traveller',
            field=models.ManyToManyField(blank=True, related_name='places', to='turism.traveller', verbose_name='Путешествие'),
        ),
    ]