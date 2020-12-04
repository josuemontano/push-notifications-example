import pendulum
from huey import MemoryHuey

from .models import SUBSCRIPTIONS
from .push import send_notification

huey =  MemoryHuey()

@huey.task()
def remind_subscriber(subscription):
    for subscription in SUBSCRIPTIONS:
        reminder = {
            "title": "Another minute passed",
            "body": pendulum.now().format('dddd DD MMMM YYYY', locale='es')
        }
        send_notification(subscription, reminder)
