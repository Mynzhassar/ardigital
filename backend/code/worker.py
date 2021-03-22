import pytz
import time

from datetime import datetime

from . import models, constants, notifications, utils


def send_notification_to_admin(cur_datetime):
    consultations = models.Consultation.objects.filter(was_sent=False)
    applications = models.Application.objects.filter(was_sent=False)

    if not consultations and not applications:
        return

    notifications.send_email(
        utils.generate_admin_text(cur_datetime, consultations.count(), applications.count()),
        constants.ARDIGITAL_EMAIL)

    consultations.update(was_sent=True)
    applications.update(was_sent=True)


def run_worker():
    while True:
        try:
            cur_datetime = datetime.utcnow().astimezone(pytz.timezone('Asia/Almaty'))

            if cur_datetime.hour in constants.HOURS_TO_SEND_EMAIL:
                send_notification_to_admin(cur_datetime)
        except Exception as e:
            print(str(e))

        time.sleep(constants.ONE_HOUR)


def main():
    run_worker()


if __name__ == '__main__':
    main()
