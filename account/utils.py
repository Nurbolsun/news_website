import pyotp
from django.utils import timezone
import logging
from django.core.mail import send_mail

from .models import Subscriber

logger = logging.getLogger(__name__)

def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    otp = totp.now()
    otp = otp[-4:]
    return otp


def subscribe_to_newsletter(email, username):
    subscriber, created = Subscriber.objects.get_or_create(email=email, username=username)
    subscriber.subscribed = True
    subscriber.unsubscribed = False
    subscriber.save()

    send_welcome_email(email, username)


def unsubscribe_from_newsletter(email):
    try:
        subscriber = Subscriber.objects.get(email=email, subscribed=True)
        subscriber.subscribed = False
        subscriber.unsubscribed = True
        subscriber.save()
        return True
    except Subscriber.DoesNotExist:
        return False


def send_newsletter_to_subscribers(newsletter):
    subscribers = Subscriber.objects.filter(subscribed=True, unsubscribed=False)

    for subscriber in subscribers:
        try:
            send_mail(
                newsletter.subject,
                newsletter.content,
                'iimgera28062004@gmail.com',
                [subscriber.email],
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке рассылки {subscriber.email}: {e}")
        else:
            subscriber.last_newsletter_sent_at = timezone.now()
            subscriber.save()

    newsletter.sent_at = timezone.now()
    newsletter.save()


def send_welcome_email(email, username):
    subject = f'Добро пожаловать в нашу рассылку, {username}!'
    message = 'Спасибо за подписку на нашу рассылку! Мы рады видеть вас среди наших подписчиков.'
    from_email = 'LifeBishkek@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
