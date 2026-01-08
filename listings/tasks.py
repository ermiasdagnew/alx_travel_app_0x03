# listings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_email, listing_title, booking_date):
    """
    Sends a booking confirmation email asynchronously.
    """
    subject = f'Booking Confirmation for {listing_title}'
    message = f'Hi,\n\nYour booking for "{listing_title}" on {booking_date} has been confirmed.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [booking_email]

    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return f"Email sent to {booking_email}"
