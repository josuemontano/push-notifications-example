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
