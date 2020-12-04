import json

from pywebpush import WebPushException, webpush

from .models import Subscription


def send_notification(subscription: Subscription, data: dict[str, str]):
    """ Generate  VAPID EC2 keys with
    openssl ecparam -name prime256v1 -genkey -noout -out private_key.pem
    """
    try:
        webpush(subscription.dict(), json.dumps(data), vapid_private_key="Ucoxpdls8HmQDx-yPUIcd8_JYx-ib9fwjkGsoB9ZcJ8", vapid_claims={"sub":"mailto:josue@magicbell.io"})
    except WebPushException as ex:
        print("I'm sorry, but I can't do that: {}", repr(ex))
