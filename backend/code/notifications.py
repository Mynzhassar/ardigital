from django.core.mail import send_mail

from . import constants


def send_email(email_info, recipient):
    send_mail(
        subject=email_info['subject'],
        message=email_info['message'],
        from_email=constants.ARDIGITAL_EMAIL,
        recipient_list=[recipient],
    )
