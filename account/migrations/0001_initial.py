# Generated by Django 5.0.1 on 2024-02-05 09:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Электронная почта')),
                ('role', models.CharField(choices=[('ADMIN', 'ADMIN'), ('SUPER_ADMIN', 'SUPER_ADMIN'), ('EDITOR', 'EDITOR'), ('JOURNALIST', 'JOURNALIST'), ('GUEST', 'GUEST')], default='GUEST', max_length=255, verbose_name='Роль')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Активный')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('gender', models.CharField(blank=True, choices=[('МУЖСКОЙ', 'МУЖСКОЙ'), ('ЖЕНСКИЙ', 'ЖЕНСКИЙ')], max_length=20, null=True, verbose_name='Пол')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
