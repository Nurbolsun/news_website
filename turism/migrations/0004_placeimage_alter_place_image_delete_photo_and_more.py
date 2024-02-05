# Generated by Django 4.2.7 on 2024-01-30 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turism', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/turism/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Изображение места',
                'verbose_name_plural': 'Изображения мест',
            },
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/turism/', verbose_name='Фото'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='turism.place', verbose_name='Место'),
        ),
    ]