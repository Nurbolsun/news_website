from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Newsletter
from .utils import send_newsletter_to_subscribers


@receiver(post_save, sender=Newsletter)
def send_newsletter_on_creation(sender, instance, created, **kwargs):
    if created:
        send_newsletter_to_subscribers(instance)
