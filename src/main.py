from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .models import SUBSCRIPTIONS, Subscription
from .push import send_notification

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    templates = Jinja2Templates(directory="src/templates")
    return templates.TemplateResponse("home.jinja2", {"request": request})


@app.get("/sw.js")
async def service_worker():
    return FileResponse('src/static/sw.js')


@app.post("/push/subscription")
async def create_subscription(subscription: Subscription):
    SUBSCRIPTIONS.append(subscription)

    sample_data = {
        "title": "Welcome to magicbell.io",
        "body": "Please confirm your email"
    }
    send_notification(subscription, data=sample_data)

    return {}
