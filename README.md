# push-notifications-example

Example on how to implement browser push notifications

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
poetry install

uvicorn src.main:app --reload
huey_consumer.py src.tasks.huey
```
