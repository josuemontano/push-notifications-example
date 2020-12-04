import os

import pendulum
from huey import RedisHuey, SqliteHuey

from .push import send_notification

redis_url = os.environ.get('REDIS_URL')
huey = RedisHuey(url=redis_url) if redis_url else SqliteHuey()


@huey.task()
def remind_subscriber(subscription):
    reminder = {
        "title": "Another minute passed",
        "body": pendulum.now().format('dddd DD MMMM YYYY', locale='es')
    }
    send_notification(subscription, reminder)
