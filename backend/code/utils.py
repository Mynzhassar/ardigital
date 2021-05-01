from datetime import datetime, timedelta
from . import constants


def generate_admin_text(time, consultations_count, applications_count):
    date_from, date_to = _format_time(time)
    subject = f'Количество новых заявок c {date_from} по {date_to}'

    if consultations_count and applications_count:
        message = f'Число новых заявок на консультацию: {consultations_count}. ' \
                  f'Число новых заявок: {applications_count}.'

    elif consultations_count:
        message = f'Число новых заявок на консультацию: {consultations_count}.'
    else:
        message = f'Число новых заявок: {applications_count}.'

    return {
        'subject': subject,
        'message': message,
    }


def _format_time(time):
    # e.g. с 2021-01-26 13:00:00 по 2021-01-26 13:59:59
    time = time - timedelta(hours=1)
    date_to = datetime(year=time.year, month=time.month, day=time.day,
                       hour=time.hour, minute=59, second=59)

    date_from = date_to - timedelta(hours=constants.EMAIL_SEND_PERIOD_HOURS) + timedelta(seconds=1)
    return date_from, date_to
