from pydantic import BaseModel

SUBSCRIPTIONS = []


class Subscription(BaseModel):
    endpoint: str
    keys: dict[str, str]
