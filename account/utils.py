import pyotp
from django.core.mail import send_mail

from .models import Subscriber

def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    otp = totp.now()
    otp = otp[-4:]
    return otp


def send_newsletter_to_subscribers(newsletter):
    subscribers = Subscriber.objects.filter(subscribed=True)

    for subscriber in subscribers:
        send_mail(
            newsletter.subject,
            newsletter.content,
            'iimgera28062004@gmail.com',
            [subscriber.email],
            fail_silently=False,
        )

    newsletter.sent_at = timezone.now()
    newsletter.save()
