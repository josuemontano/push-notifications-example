import pendulum
from huey import SqliteHuey

from .push import send_notification

huey = SqliteHuey(filename='huey.db')


@huey.task()
def remind_subscriber(subscription):
    reminder = {
        "title": "Another minute passed",
        "body": pendulum.now().format('dddd DD MMMM YYYY', locale='es')
    }
    send_notification(subscription, reminder)
