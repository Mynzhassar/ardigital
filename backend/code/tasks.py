import pytz
import redis

from datetime import datetime
from workers import task

from . import models, constants, notifications, utils

redis_db = redis.Redis()


def send_notification_to_admin(cur_datetime):
    if cur_datetime.hour not in constants.HOURS_TO_SEND_EMAIL:
        return

    redis_key = cur_datetime.strftime(constants.REDIS_KEY_DATETIME_FORMAT)
    was_notified = redis_db.get(redis_key)

    if was_notified:
        return

    redis_db.setex(redis_key, constants.REDIS_KEY_TTL, 1)

    consultations = models.Consultation.objects.filter(was_notified=False)
    applications = models.Application.objects.filter(was_notified=False)

    if not consultations and not applications:
        return

    notifications.send_email(
        utils.generate_admin_text(cur_datetime, consultations.count(), applications.count()),
        constants.ARDIGITAL_EMAIL)

    consultations.update(was_notified=True)
    applications.update(was_notified=True)


@task(schedule=constants.TEN_MINUTES)
def run_worker():
    try:
        cur_datetime = datetime.utcnow().astimezone(pytz.timezone('Asia/Almaty'))
        send_notification_to_admin(cur_datetime)
    except Exception as e:
        print(str(e))
