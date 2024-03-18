from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin

from .models import User, Newsletter, Subscriber


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = ('email', 'username')
    list_per_page = 10
    list_display = ('email', 'username',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password',)}),
        ('Профиль', {'fields': (
            'avatar',
            'role',
            'gender',
            'age',
        )}),
        ('Разрешения', {'fields': (
            'is_active',
            'is_staff',
        )}),
    )


@admin.register(Subscriber)
class SubscriberAdmin(ModelAdmin):
    list_display = (
        'email',
        'username',
        'subscribed',
        'unsubscribed',
    )


@admin.register(Newsletter)
class NewsletterAdmin(ModelAdmin):
    list_display = (
        'subject',
        'content',
        'sent_at',
    )